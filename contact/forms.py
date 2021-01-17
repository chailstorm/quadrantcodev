from django import forms
from .models import contacts

class contactUs(forms.ModelForm):
	class Meta:
		model = contacts
		fields = ['name','email','comment']