from django.shortcuts import render, redirect
import sqlite3
import datetime as dt
import numpy as np
from django.contrib import messages
from django.contrib.auth import forms
from solutions.models import qinfo
from userlogin.models import Qstripe
from quadrantco.settings import DATABASES
from profiles.models import avail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from userlogin.models import clientprofile
import http.client
import json
import datetime as dt
import time
from quadrantco.settings import ZOOM
from authlib.jose import jwt
from quadrantco.settings import STRIPE
import stripe

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import numpy as np
from .models import forwards
from .forms import forwardQA
from django.conf import settings

# Create your views here.

class ZoomError(Exception):
	pass
		
class scheduler():
	@login_required
	def confirm(request,qid,year,month,day,start,end):
		uid = request.user.id
		filter_kwargs = {
			'qn__exact': qid,
			}
		qdata = qinfo.objects.filter(**filter_kwargs)
		rate = qdata[0].cost
		
		time1 = dt.datetime.strptime(start, "%I:%M %p")
		time3 = dt.datetime.strptime(end, "%I:%M %p")
		if time3>time1:
			length = time3 - time1
			minutes = length.seconds/60
			hours = minutes/60
		cost = int(np.ceil(rate*hours))
		
		
		context = {
			'q': qdata[0],
			'year': year,
			'month': month,
			'day': day,
			'start': start,
			'end': end,
			'cost':cost
			}
		
		if request.method=='POST':
			desc = request.POST.get('field')
			
			filter_kwargs = {
				'qn__exact': qid,
				'year__exact': year,
				'month__exact': month,
				'date__exact': day,
				'start__exact': start,
				}
			slot = avail.objects.filter(**filter_kwargs)[0]
			slot.status = 2
			slot.cn = uid
			slot.description = desc
			slot.cost = cost
			slot.save()
			
			return redirect('checkout',qid=qid,year=year,month=month,day=day,start=start,end=end)
		
		return render(request, 'schedule.html',context=context)
	
	@login_required
	def cancel(request,uid,year,month,day,start):
		try:
			cdata = clientprofile.objects.get(user_id=uid)
			cn = uid
			filter_kwargs = {
				'cn__exact': cn,
				'year__exact': year,
				'month__exact': month,
				'date__exact': day,
				'start__exact': start,
				}
			slot = avail.objects.filter(**filter_kwargs)[0]
			qn = slot.qn
		except Exception:
			qdata = qinfo.objects.get(qn=uid)
			qn = uid
			filter_kwargs = {
				'qn__exact': qn,
				'year__exact': year,
				'month__exact': month,
				'date__exact': day,
				'start__exact': start,
				}
			slot = avail.objects.filter(**filter_kwargs)[0]
			cn = slot.cn
		
		user_uids = [qn,cn]
		if request.user.id in user_uids:
			now = dt.datetime.now()
			if request.method=="POST":
				#Perform refund through stripe
				stripe.api_key = STRIPE['SECRET']
				refund = stripe.Refund.create(payment_intent=slot.orderid)
				refund_id = refund['id']
				
				#Cancel meeting in Zoom
				code = zoom.cancelMeeting(slot.meetingid)
				
				slot.status = 1
				slot.orderid = refund_id
				slot.cn = 0
				slot.description = "refunded"
				slot.meetingid = 0
				slot.joinurl = ""
				slot.password = ""
				slot.curl = ""
				slot.qurl = ""
				slot.save()
				
				context = {'qn': qn,'now': now.strftime('%Y-%m-%d')}
				
				#Send an email to both client and Q to confirm and notify them of the cancelation. 
				
				return render(request,'canceled.html',context=context)
			else:
				context = {
					'q': qinfo.objects.get(qn=qn),
					'year': year,
					'month': month,
					'day': day,
					'start': start,
					'end': slot.end,
					'cost': slot.cost,
					'uid': uid,
					}
				return render(request,'cancelconfirm.html',context=context)
		else:
			return redirect('userloginerror')
			
	
	@login_required
	def forward(request,qid,year,month,day,start):
		qdata = qinfo.objects.get(qn=qid)
		filter_kwargs = {
			'qn__exact': qid,
			'year__exact': year,
			'month__exact': month,
			'date__exact': day,
			'start__exact': start,
			}
		slot = avail.objects.filter(**filter_kwargs)[0]
		
		forwardform = forwardQA
		if request.method=="POST":
			forwardform = forwardQA(data=request.POST)
			if forwardform.is_valid():
				name = forwardform.cleaned_data.get('name')
				#email = forwardform.cleaned_data.get('email')
				name = name.replace(" ","_")
				
				fwd = forwardform.save(commit=False)
				fwd.name = name
				fwd.qn = qid
				fwd.year = year
				fwd.month = month
				fwd.date = day
				fwd.start = start
				
				values = {
					'name': name,
					'meeting': {
						'date': str(year)+'-'+str(month)+'-'+str(day),
						'time': start,
						'url': settings.ADDRESS+'join/meeting/'+name+'/'+str(slot.meetingid)+'/'+str(slot.password)
						}
					}
				fwd.url = values['meeting']['url']
				fwd.save()
				#subject = 'You''ve been invited!'
				#html_message = render_to_string('meeting/email.html',values)
				#plain_message = strip_tags(html_message)
				#from_email = 'coltjames.hail@gmail.com'
				#f_email = email
				#mail.send_mail(subject,plain_message,from_email,[f_email],html_message=html_message)
				messages.info(request, "Invite forwarded sucessfully. Forward to another participant if you wish.")
		
		context = {
			'qn': qid,
			'year': year,
			'month': month,
			'day': day,
			'start': start,
			'forwardform': forwardform,
			}
		return render(request,'forward.html',context=context)
		

class zoom():
	conn = http.client.HTTPSConnection("api.zoom.us")
	host_id = 'A67ct1ExR1WxfiL72rBzCQ'
	
	def getJWT():
		header = {'alg': 'HS256', 'typ': 'JWT'}
		payload = {'iss': ZOOM['KEY'], 'exp': int(time.time())+120}
		s = jwt.encode(header,payload,ZOOM['SECRET'])
		ss = s.decode('utf-8')
		return ss
	
	def genHeaders():
		jwt = zoom.getJWT()
		headers = {
			'authorization': "Bearer " + jwt,
			'content-type': "application/json"
			}
		return headers
	
	def scheduleMeeting(host_id,start,desc):
		url = "/v2/users/" + host_id + "/meetings"
		body = {
			'topic': 'Q and A',
			'start_time': start,
			'timezone': 'America/Chicago',
			'password': 'quadco',
			'agenda': desc,
			'settings': {
				'host_video': True,
				'join_before_host': True,
				'mute_upon_entry': False,
				'approval_type': '2'
				}
			}
		
		headers = zoom.genHeaders()
		zoom.conn.request("POST",url,headers=headers,body=bytes(json.dumps(body), encoding="utf-8"))
		res = zoom.conn.getresponse()
		data = res.read()
		zoom.conn.close()
		r = data.decode("utf-8")
		rs = json.loads(r)
		
		return rs
	
	def cancelMeeting(meetingid):
		url = "/v2" + "/meetings/" + str(meetingid)
		headers = zoom.genHeaders()
		t = zoom.conn.request("DELETE",url,headers=headers)
		res = zoom.conn.getresponse()
		code = res.status
		return code


class checkout():
	def payment(request,qid,year,month,day,start,end):
		uid = request.user.id
		
		
		filter_kwargs = {
			'qn__exact': qid,
			'year__exact': year,
			'month__exact': month,
			'date__exact': day,
			'start__exact': start,
			}
		slot = avail.objects.filter(**filter_kwargs)[0]
		
		cost = slot.cost
		
		context = {
			'qn': qid,
			'year': year,
			'month': month,
			'day': day,
			'start': start,
			'end': end,
			'cost':cost
			}
		
		
		return render(request, 'checkout.html',context=context)
		
	
	@csrf_exempt
	def createpayment(request):
		if request.user.is_authenticated:
			
			stripe.api_key = STRIPE['SECRET']
			if request.method=="POST":
				
				data = json.loads(request.body)
				#Insert pulling data from request here:
				qid = int(data['qn'])
				year = int(data['year'])
				month = int(data['month'])
				day = int(data['day'])
				start = data['start']
				
				filter_kwargs = {
					'qn__exact': qid,
					'year__exact': year,
					'month__exact': month,
					'date__exact': day,
					'start__exact': start,
					}
				slot = avail.objects.filter(**filter_kwargs)[0]
				
				cost = slot.cost*100
				fee = int(np.ceil(cost*0.20))
				
				filter_kwargs = {
					'qn__exact': qid,
					}
				acct = Qstripe.objects.filter(**filter_kwargs)
				acct_id = acct[0].acct_id
				
				# Create a PaymentIntent with the order amount and currency
				intent = stripe.PaymentIntent.create(
				  payment_method_types=['card'],
				  amount=cost,
				  currency='usd',
				  application_fee_amount=fee,
				  transfer_data={
					'destination': acct_id,
				  })
				
				try:
					return JsonResponse({'publishableKey':	
						STRIPE['KEY'], 'clientSecret': intent.client_secret})
				except Exception as e:
					return JsonResponse({'error':str(e)},status= 403)
	
	
	def paymentcomplete(request):
		if request.method=="POST":
			data = json.loads(request.POST.get("payload"))
			order = json.loads(request.POST.get("body"))
			if data["status"]=="succeeded":
				orderid = data['id']
				qid = int(order['qn'])
				year = int(order['year'])
				month = int(order['month'])
				day = int(order['day'])
				start = order['start']
				
				#Pull user and q data
				uid = request.user.id
				filter_kwargs = {
					'qn__exact': qid,
					}
				qdata = qinfo.objects.filter(**filter_kwargs)
				qdata = qdata[0]
				
				#Pull description for meeting
				filter_kwargs = {
					'qn__exact': qid,
					'year__exact': year,
					'month__exact': month,
					'date__exact': day,
					'start__exact': start,
					}
				slot = avail.objects.filter(**filter_kwargs)[0]
				desc = slot.description
				#Schedule meeting
				time1 = dt.datetime.strptime(start, "%I:%M %p")
				time2 = dt.time.strftime(time1.time(), "%H:%M")
				startstr = str(year)+'-'+str(month)+'-'+str(day)+'T'+time2+':00'
				try: 
					
					rs = zoom.scheduleMeeting(zoom.host_id,startstr,desc)
					rs_id = rs['id']
					rs_url = rs['join_url']
					rs_pass = rs['password']
				except Exception as ex:
					raise ZoomError(ex)
				
				
				#Send two emails. One to the client with their link, and one to the Q with their link. Only difference is the name & email in the SDK URL.
				#Later I can add the link to the user profiles, first I need to create a C/Q differentiator in the user signup.
				
				#client values
				values = {
					'name': qdata.first + ' ' + qdata.last,
					'meeting': {
						'date': str(year)+'-'+str(month)+'-'+str(day),
						'time': start,
						'url': settings.ADDRESS+'join/meeting/'+request.user.username+'/'+str(rs_id)+'/'+str(rs_pass)
						}
					}
					
				#subject = 'Your Q&A Session'
				#html_message = render_to_string('meeting/email.html',values)
				#plain_message = strip_tags(html_message)
				#from_email = 'coltjames.hail@gmail.com'
				#c_email = request.user.email
				#mail.send_mail(subject,plain_message,from_email,[c_email],html_message=html_message)
				c_url = values['meeting']['url']
				#Q values
				#q_email = qdata.email
				values['meeting']['url'] = settings.ADDRESS+'join/meeting/'+qdata.first+'_'+qdata.last+'/'+str(rs_id)+'/'+str(rs_pass)
				#html_message = render_to_string('meeting/email.html',values)
				#plain_message = strip_tags(html_message)
				#mail.send_mail(subject,plain_message,from_email,[q_email],html_message=html_message)
				q_url = values['meeting']['url']
				#Update avail db
				
				slot.status = 3
				slot.meetingid = rs_id
				slot.joinurl = rs_url
				slot.password = rs_pass
				slot.orderid = orderid
				slot.curl = c_url
				slot.qurl = q_url
				slot.confirmedEmail = 1
				slot.canceledEmail = 1
				slot.save()
				
				
				return render(request,'paymentcomplete.html')
			else:
				return render(request, 'index.html')
