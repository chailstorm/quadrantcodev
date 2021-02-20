from django.shortcuts import render, redirect
from solutions.models import qinfo
from userlogin.models import clientprofile
from blog.models import post
import datetime as dt
import sqlite3
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import recuravail, individualavail
from .models import avail,recur
# Create your views here.


class qprofile():
	model = qinfo
	template_name = 'user.html'
	
	def freeIndys(getq,date):
		filter_kwargs = {
					'qn__exact': getq,
					'year__exact': date.year,
					'month__exact': date.month,
					'date__exact': date.day,
					'status__exact': 1,
					}
		objs = avail.objects.filter(**filter_kwargs)
		return objs
	
	#@login_required
	def get_q(request, getq, availstart):
		date = dt.datetime.strptime(availstart,'%Y-%m-%d')
		startdate = date
		filter_kwargs = {
			'qn__exact': getq,
			}
		qdata = qinfo.objects.filter(**filter_kwargs)
		
		#Pull available time slots
		#first day
		first = {'year':date.year,'month':date.month,'day':date.day}
		objs = qprofile.freeIndys(getq,date)
		firststarts = qprofile.orderIndys(objs)
		#second day
		date = date + dt.timedelta(days=1)
		second = {'year':date.year,'month':date.month,'day':date.day}
		objs = qprofile.freeIndys(getq,date)
		secondstarts = qprofile.orderIndys(objs)
		#third day
		date = date + dt.timedelta(days=1)
		third = {'year':date.year,'month':date.month,'day':date.day}
		objs = qprofile.freeIndys(getq,date)
		thirdstarts = qprofile.orderIndys(objs)
		#fourth day
		date = date + dt.timedelta(days=1)
		fourth = {'year':date.year,'month':date.month,'day':date.day}
		objs = qprofile.freeIndys(getq,date)
		fourthstarts = qprofile.orderIndys(objs)
		#fifth day
		date = date + dt.timedelta(days=1)
		fifth = {'year':date.year,'month':date.month,'day':date.day}
		objs = qprofile.freeIndys(getq,date)
		fifthstarts = qprofile.orderIndys(objs)
		#sixth day
		date = date + dt.timedelta(days=1)
		sixth = {'year':date.year,'month':date.month,'day':date.day}
		objs = qprofile.freeIndys(getq,date)
		sixthstarts = qprofile.orderIndys(objs)
		#seventh day
		date = date + dt.timedelta(days=1)
		seventh = {'year':date.year,'month':date.month,'day':date.day}
		objs = qprofile.freeIndys(getq,date)
		seventhstarts = qprofile.orderIndys(objs)
		
		avails = {
			'first': first,
			'firststarts': firststarts,
			'second': second,
			'secondstarts': secondstarts,
			'third': third,
			'thirdstarts':thirdstarts,
			'fourth': fourth,
			'fourthstarts': fourthstarts,
			'fifth': fifth,
			'fifthstarts': fifthstarts,
			'sixth': sixth,
			'sixthstarts': sixthstarts,
			'seventh': seventh,
			'seventhstarts': seventhstarts
			}
		
		prevweek = startdate - dt.timedelta(days=7)
		prevweek = prevweek.strftime('%Y-%m-%d')
		nextweek = startdate + dt.timedelta(days=7)
		nextweek = nextweek.strftime('%Y-%m-%d')
		
		filter_kwargs = {
			'author__exact': getq,
			'status__exact': 1
			}
		posts = post.objects.filter(**filter_kwargs)
		
		context = {
			'q': qdata[0],
			'avails': avails,
			'prevweek': prevweek,
			'nextweek': nextweek,
			'blogposts': posts
			}
		return render(request, 'user.html', context=context)
		
	def dt24hrTime(strtime):
		time1 = dt.datetime.strptime(strtime, "%I:%M %p")
		return time1.time()
	def str12hrTime(timeobj):
		time2 = dt.time.strftime(timeobj,"%I:%M %p")
		return time2
	
	
	@login_required
	def account(request, getq):
		if int(request.user.id)==int(getq):
			try:
				qdata = qinfo.objects.get(qn=request.user.id)
				
				filter_kwargs = {
					'author__exact': getq,
					}
				posts = post.objects.filter(**filter_kwargs)
				
				
				#conn,c = qprofile.openConn()
				#c.execute("""SELECT * FROM avail WHERE qn=? AND status=3""",(getq,))
				#conn.commit()
				#rqas = c.fetchall()
				#conn.close()
				
				#Converting to model based avail
				filter_kwargs = {
					'qn__exact': getq,
					'status__exact': 3,
					}
				rqas = avail.objects.filter(**filter_kwargs)
				
				qas = []
				links = []
				ii = 0
				jj = 0
				while jj<len(rqas):
					try:
						date = str(rqas[ii].month)+'/'+str(rqas[ii].date)+'/'+str(rqas[ii].year)
						cn = int(rqas[ii].cn)
						c = User.objects.get(id=cn)
						name = c.first_name + ' ' + c.last_name
						r = {'text': date + ' at ' + rqas[ii].start + ' with ' + name,'link': rqas[ii].qurl,'year':rqas[ii].year,'month':rqas[ii].month,'date':rqas[ii].date,'start':rqas[ii].start}
						qas.append(r)
						ii += 1
						jj += 1
					except Exception:
						jj += 1
				now = dt.datetime.now()
				now = now.strftime('%Y-%m-%d')
				context = {
					'q': qdata,
					'blogposts': posts,
					'qas': qas,
					'now': now
					}
					
				return render(request, 'qedit.html', context=context)
			except Exception:
				cdata = clientprofile.objects.get(user_id=request.user.id)
				cuser = User.objects.get(id=request.user.id)
				filter_kwargs = {
					'author__exact': getq,
					}
				posts = post.objects.filter(**filter_kwargs)
				
				#conn,c = qprofile.openConn()
				#c.execute("""SELECT * FROM avail WHERE cn=?""",(getq,))
				#conn.commit()
				#rqas = c.fetchall()
				#conn.close()
				filter_kwargs = {
					'cn__exact': getq
					}
				rqas = avail.objects.filter(**filter_kwargs)
				qas = []
				ii = 0
				jj = 0
				while jj<len(rqas):
					try:
						date = str(rqas[ii].month)+'/'+str(rqas[ii].date)+'/'+str(rqas[ii].year)
						qn = int(rqas[ii].qn)
						q = qinfo.objects.get(qn=qn)
						name = q.__str__()
						r = {'text': date + ' at ' + rqas[ii].start + ' with ' + name,'link': rqas[ii].curl,'qn':qn,'year':rqas[ii].year,'month':rqas[ii].month,'date':rqas[ii].date,'start':rqas[ii].start}
						qas.append(r)
						ii += 1
						jj += 1
					except Exception:
						jj += 1
				
				now = dt.datetime.now()
				now = now.strftime('%Y-%m-%d')
				context = {
					'c': cdata,
					'name': cuser.first_name + ' ' + cuser.last_name,
					'cn': request.user.id,
					'blogposts': posts,
					'qas': qas,
					'now': now
					}
				
				return render(request, 'cedit.html', context=context)
		else:
			now = dt.datetime.now()
			now = now.strftime('%Y-%m-%d')
			return redirect('profiles',getq=getq,availstart=now)
	
	def activeIndys(getq,date):
		filter_kwargs = {
					'qn__exact': getq,
					'year__exact': date.year,
					'month__exact': date.month,
					'date__exact': date.day,
					}
		objs = avail.objects.filter(**filter_kwargs) #.exclude(status=0)
		return objs
	
	def orderIndys(objs):
		firststarts = [0]*len(objs)
		if len(objs)>0:
			for start in range(0,len(objs)):
				firststarts[start] = [objs[start].start,objs[start].end,objs[start].year,objs[start].month,objs[start].date,objs[start].status]
		
		if len(firststarts)>0:
			datetimes = [0]*len(firststarts)
			for start in range(0,len(firststarts)):
				datetimes[start] = [qprofile.dt24hrTime(firststarts[start][0]),qprofile.dt24hrTime(firststarts[start][1]),objs[start].year,objs[start].month,objs[start].date,objs[start].status]
			datetimes = sorted(datetimes,key=lambda x: x[1])
			for start in range(0,len(firststarts)):
				firststarts[start] =  {'starttime': qprofile.str12hrTime(datetimes[start][0]),
					'endtime': qprofile.str12hrTime(datetimes[start][1]),
					'year': datetimes[start][2],
					'month': datetimes[start][3],
					'date': datetimes[start][4],
					'status': datetimes[start][5],
					}
		else:
			firststarts = {}
		
		return firststarts
			
	
	@login_required
	def setAvail(request, getq, availstart):
		getq = int(getq)
		now = dt.datetime.now()
		now_dt = now
		now = now.strftime('%Y-%m-%d')
		if int(request.user.id)==getq:
			recurform = recuravail
			indyform = individualavail
			
			if request.method=="POST":
				if 'recuravail' in request.POST:
					recurform = recuravail(data=request.POST)
					if recurform.is_valid():
						day = recurform.cleaned_data.get('day')
						hour = int(recurform.cleaned_data.get('hour'))
						if hour<10:
							strhour = '0' + str(hour)
						else:
							strhour = str(hour)
						minute = recurform.cleaned_data.get('minute')
						half = recurform.cleaned_data.get('half')
						start = strhour + ':' + str(minute) + ' ' + str(half)
						
						obj = recur.objects.create(qn=int(request.user.id),day=day,start=start,length=60)
						
						return redirect('availability',getq=getq,availstart=availstart)
				elif 'indyavail' in request.POST:
					indyform = indyform(data=request.POST)
					if indyform.is_valid():
						month = indyform.cleaned_data.get('month')
						date = indyform.cleaned_data.get('date')
						hour = int(indyform.cleaned_data.get('hour'))
						if hour<10:
							strhour = '0' + str(hour)
						else:
							strhour = str(hour)
						minute = indyform.cleaned_data.get('minute')
						half = indyform.cleaned_data.get('half')
						
						#Determine year
						year = now_dt.year
						indy_str = str(year)+'-'+str(month)+'-'+str(date)+' '+str(hour)+':'+str(minute)+':00'+' '+half
						indy_dt = dt.datetime.strptime(indy_str,'%Y-%m-%d %I:%M:%S %p')
						if indy_dt<now_dt:
							year += 1
							indy_str = str(year)+'-'+str(month)+'-'+str(date)+' '+str(hour)+':'+str(minute)+':00'+' '+half
							indy_dt = dt.datetime.strptime(indy_str,'%Y-%m-%d %I:%M:%S %p')
						start = strhour + ':' + str(minute) + ' ' + str(half)
						end_dt = indy_dt + dt.timedelta(minutes=60)
						end = end_dt.strftime('%I:%M %p')
						
						filter_kwargs = {
							'qn__exact': int(request.user.id),
							'year__exact': year,
							'month__exact': month,
							'date__exact': date,
							'start__exact': start,
							}
						objs = avail.objects.filter(**filter_kwargs)
						if len(objs)==0:	
							obj = avail.objects.create(qn=int(request.user.id),year=year,month=month,date=date,start=start,end=end,status=1)
						
						return redirect('availability',getq=getq,availstart=availstart)
			
			#Pull avails
			#first day
			date = dt.datetime.strptime(availstart,'%Y-%m-%d')
			startdate = date
			first = {'year':date.year,'month':date.month,'day':date.day}
			objs = qprofile.activeIndys(getq,date)
			firststarts = qprofile.orderIndys(objs)
			#second day
			date = date + dt.timedelta(days=1)
			second = {'year':date.year,'month':date.month,'day':date.day}
			objs = qprofile.activeIndys(getq,date)
			secondstarts = qprofile.orderIndys(objs)
			#third day
			date = date + dt.timedelta(days=1)
			third = {'year':date.year,'month':date.month,'day':date.day}
			objs = qprofile.activeIndys(getq,date)
			thirdstarts = qprofile.orderIndys(objs)
			#fourth day
			date = date + dt.timedelta(days=1)
			fourth = {'year':date.year,'month':date.month,'day':date.day}
			objs = qprofile.activeIndys(getq,date)
			fourthstarts = qprofile.orderIndys(objs)
			#fifth day
			date = date + dt.timedelta(days=1)
			fifth = {'year':date.year,'month':date.month,'day':date.day}
			objs = qprofile.activeIndys(getq,date)
			fifthstarts = qprofile.orderIndys(objs)
			#sixth day
			date = date + dt.timedelta(days=1)
			sixth = {'year':date.year,'month':date.month,'day':date.day}
			objs = qprofile.activeIndys(getq,date)
			sixthstarts = qprofile.orderIndys(objs)
			#seventh day
			date = date + dt.timedelta(days=1)
			seventh = {'year':date.year,'month':date.month,'day':date.day}
			objs = qprofile.activeIndys(getq,date)
			seventhstarts = qprofile.orderIndys(objs)
			
			avails = {
				'first': first,
				'firststarts': firststarts,
				'second': second,
				'secondstarts': secondstarts,
				'third': third,
				'thirdstarts':thirdstarts,
				'fourth': fourth,
				'fourthstarts': fourthstarts,
				'fifth': fifth,
				'fifthstarts': fifthstarts,
				'sixth': sixth,
				'sixthstarts': sixthstarts,
				'seventh': seventh,
				'seventhstarts': seventhstarts,
				}
				
			prevweek = startdate - dt.timedelta(days=7)
			prevweek = prevweek.strftime('%Y-%m-%d')
			nextweek = startdate + dt.timedelta(days=7)
			nextweek = nextweek.strftime('%Y-%m-%d')
			
			#Fetch recuring times to send to the frontend
			days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
			recurs = {}
			for day in days:
				filter_kwargs = {
					'qn__exact': getq,
					'day__exact': day,
					}
				objs = recur.objects.filter(**filter_kwargs)
				starts = [0]*len(objs)
				if len(objs)>0:
					for start in range(0,len(objs)):
						starts[start] = [objs[start].start,objs[start].length]
				if len(starts)>0:
					datetimes = [0]*len(starts)
					for start in range(0,len(starts)):
						#startTime = qprofile.dt24hrTime(starts[start][0])
						startTime = dt.datetime.strptime(starts[start][0],'%I:%M %p')
						length = int(starts[start][1])
						endtime = startTime + dt.timedelta(minutes=length)
						#endtime = endtime.strftime('%I:%M %p')
						datetimes[start] = [startTime.time(),endtime.time()]
					datetimes = sorted(datetimes,key=lambda x: x[1])
					for start in range(0,len(starts)):
						starts[start] =  {'starttime': qprofile.str12hrTime(datetimes[start][0]),
							'endtime': qprofile.str12hrTime(datetimes[start][1])}
				else:
					starts = {}
					
				recurs[day] = starts
				
			
			
			
			context = {
				'avails': avails,
				'prevweek': prevweek,
				'nextweek': nextweek,
				'qn': getq,
				'now': now,
				'recurform': recurform,
				'indyform': indyform,
				'recurs': recurs,
				}
			return render(request, 'setavail.html', context=context)
		else:
			return redirect('profiles',getq=getq,availstart=now)
	
	@login_required
	def unsetAvail(request, getq, availstart, year, month, date, starttime):
		getq = int(getq)
		now = dt.datetime.now()
		now_dt = now
		now = now.strftime('%Y-%m-%d')
		start = starttime
		if int(request.user.id)==getq:
			filter_kwargs = {
				'qn__exact': getq,
				'year__exact': year,
				'month__exact': month,
				'date__exact': date,
				'start__exact': start,
				}
			slot = avail.objects.filter(**filter_kwargs)[0]
			if slot.status==1:
				slot.status = 0
				slot.save()
			elif slot.status==0:
				slot.status = 1
				slot.save()
			else:
				return redirect('cancel',uid=getq,year=year,month=month,day=date,start=start)
			return redirect('availability',getq=getq,availstart=availstart)
		else:
			return redirect('profiles',getq=getq,availstart=now)