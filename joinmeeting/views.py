from django.shortcuts import render
from django.shortcuts import redirect
from quadrantco.settings import ZOOM
import hashlib
import hmac
import base64
import time
from django.conf import settings

# Create your views here.
class joinmeeting():
	def join(request,uname,mn,mp):
		apikey = ZOOM['KEY']
		data = {'apiKey': apikey ,
			'apiSecret': ZOOM['SECRET'],
			'meetingNumber': int(mn),
			'role': 0}
		signature = joinmeeting.generateSignature(data)
		join_url = settings.ADDRESS+'meeting.html/?name='+uname+'&mn='+mn+'&email='+'&pwd='+mp+'&role=0&lang=en-US&signature='+signature+'&china=0&apiKey='+apikey
		return redirect(join_url)
	
	def generateSignature(data):
		ts = int(round(time.time() * 1000)) - 30000;
		msg = data['apiKey'] + str(data['meetingNumber']) + str(ts) + str(data['role']);    
		message = base64.b64encode(bytes(msg, 'utf-8'));
		# message = message.decode("utf-8");    
		secret = bytes(data['apiSecret'], 'utf-8')
		hash = hmac.new(secret, message, hashlib.sha256);
		hash =  base64.b64encode(hash.digest());
		hash = hash.decode("utf-8");
		tmpString = "%s.%s.%s.%s.%s" % (data['apiKey'], str(data['meetingNumber']), str(ts), str(data['role']), hash);
		signature = base64.b64encode(bytes(tmpString, "utf-8"));
		signature = signature.decode("utf-8");
		return signature.rstrip("=");