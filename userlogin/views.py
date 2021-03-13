from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
import stripe
from quadrantco.settings import STRIPE
import datetime as dt
import string
import random
from .forms import createUserForm
from .forms import createUserProfile
from .forms import createQprofile
from .forms import createQphoto
from .forms import passwordReset
from .models import Qstripe, QregStr, clientprofile, passwordreset
from solutions.models import qinfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.
def gotoLogin(request):
	form = AuthenticationForm
	if request.method=='POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				#messages.info(request, f"You are now logged in as {username}")
				return redirect('index')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
			
	context = {'form': form}
	return render(request, 'registration/login.html', context)

def gotoLoginError(request):
	form = AuthenticationForm
	if request.method=='POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('index')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	else:
		messages.error(request, "You must be logged in to view this page")
	context = {'form': form}
	return render(request, 'registration/login.html', context)
	
def goLogout(request):
	auth.logout(request)
	return redirect('index')
	
def register(request):
	form = createUserForm
	profileform = createUserProfile
	uploadPhoto = createQphoto
	if request.method=='POST':
		form = createUserForm(request.POST)
		profileform = createUserProfile(request.POST)
		uploadPhoto = createQphoto(request.POST, request.FILES)
		if form.is_valid() and profileform.is_valid():
			user = form.save()
			
			profile = profileform.save(commit=False)
			profile.user = user
			profile.save()
			
			user = form.cleaned_data.get('username')
			#from django.contrib.auth.models import User
			userinfo = User.objects.get(username=user)
			uid = userinfo.id
			
			if uploadPhoto.is_valid():
				photo = uploadPhoto.save(commit=False)
				photo.user = userinfo
				photo.pid = uid
				photo.profile_image = uploadPhoto.cleaned_data.get('profile_image')
				photo.save()
			
			
			messages.success(request, 'Account created for ' + user)
			return redirect('userlogin')
	
	
	context = {
		'form': form,
		'profileform': profileform,
		'uploadPhoto': uploadPhoto,
		}
	return render(request, 'registration/clientregister.html', context)

def qregister(request, regStr):
	filter_kwargs = {
	'code__exact': regStr,
	}
	try:
		code = QregStr.objects.filter(**filter_kwargs)
		code = code[0]
		status = code.status
	except Exception:
		status = 1
	if status==0:
		form = createUserForm
		profileform = createQprofile
		uploadPhoto = createQphoto
		if request.method=='POST':
			form = createUserForm(request.POST)
			profileform = createQprofile(request.POST)
			uploadPhoto = createQphoto(request.POST, request.FILES)
			if form.is_valid() and profileform.is_valid():
				user = form.save()
				profile = profileform.save(commit=False)
				profile.user = user
				
				user = form.cleaned_data.get('username')
				#from django.contrib.auth.models import User
				userinfo = User.objects.get(username=user)
				uid = userinfo.id
				profile.qn = uid
				profile.first = userinfo.first_name
				profile.last = userinfo.last_name
				profile.email =  userinfo.email
				profile.category = 'medicine'
				profile.save()
				
				code.status = 1
				code.assigned = uid
				code.save()
				
				if uploadPhoto.is_valid():
					photo = uploadPhoto.save(commit=False)
					photo.user = userinfo
					photo.pid = uid
					photo.profile_image = uploadPhoto.cleaned_data.get('profile_image')
					photo.save()
				
				messages.success(request, 'Q Account created for ' + user)
				#Stripe section
				stripe.api_key = STRIPE['SECRET']
				account = stripe.Account.create(type='express',)
				account_id = account['id']
				
				obj = Qstripe.objects.create(qn=uid,acct_id=account_id)
				
				account_link = stripe.AccountLink.create(
					account= account_id,
					refresh_url=settings.ADDRESS+'userlogin/',
					return_url=settings.ADDRESS+'userlogin/',
					type='account_onboarding',
					)
				account_link_url = account_link['url']
				
				return redirect(account_link_url)
				
		context = {
			'form': form,
			'profileform': profileform,
			'uploadPhoto': uploadPhoto,
			'regStr': regStr,
			}
		return render(request, 'registration/qregister.html', context)
	else: 
		return redirect('userlogin')
@login_required
def qprofileUpdate(request):
	instance = get_object_or_404(qinfo, qn=request.user.id)
	profileform = createQprofile(request.POST or None, instance=instance)
	context = {
		'profileform': profileform,
		}
	if profileform.is_valid():
		profileform.save()
		
		return redirect('account', getq=request.user.id) 
	return render(request, 'registration/qupdate.html', context)
	
@login_required
def cprofileUpdate(request):
	instance = get_object_or_404(clientprofile, user_id=request.user.id)
	profileform = createUserProfile(request.POST or None, instance=instance)
	context = {
		'profileform': profileform,
		}
	if profileform.is_valid():
		profileform.save()
		
		return redirect('account', getq=request.user.id)  
	return render(request, 'registration/cupdate.html', context)

def forgotPassword(request):
	resetform = passwordReset
	if request.method=='POST':
		resetform = passwordReset(request.POST)
		if resetform.is_valid():
			reset = resetform.save(commit=False)
			letters = string.ascii_lowercase
			result_str = ''.join(random.choice(letters) for i in range(10))
			reset.codestr = result_str
			
			link = settings.ADDRESS+'userlogin/resetpassword/'+result_str
			reset.url = link
			reset.save()
			return render(request, 'registration/passwordresetsent.html', context={})
	return render(request, 'registration/passwordreset.html', context={'resetform': resetform})

def resetPassword(request, resetStr):
	return render(request, 'registration/passwordresetsent.html', context={})
