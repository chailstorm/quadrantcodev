from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import clientprofile, Qphoto, passwordreset
from solutions.models import qinfo


class createUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','email','username','password1','password2']
	
class createUserProfile(forms.ModelForm):
	class Meta:
		model = clientprofile
		fields = ['position','company','location']
	
class createQprofile(forms.ModelForm):
	class Meta:
		model = qinfo
		fields = [
			'active',
			'prefix',
			'suffix',
			'servicelinedev',
			'capitalplan',
			'pysicianrecruitment',
			'processimprove',
			'productivity',
			'operationsfinance',
			'leadingmeetings',
			'dataanalysis',
			'teamcourses',
			'personalleadership',
			'personalitytypes',
			'tempassignments',
			'special1',
			'special2',
			'special3',
			'special4',
			'special5',
			'description',
			'bio',
			'linkedin',
			'yearexp',
			'cost'
			]

class createQphoto(forms.ModelForm):
	class Meta:
		model = Qphoto
		fields = ['profile_image']


class passwordReset(forms.ModelForm):
	class Meta:
		model = passwordreset
		fields = ['username']

#class resetPassword(forms.ModelForm):
#	class Meta:
#		model = User
#		fields = ['password1','password2']