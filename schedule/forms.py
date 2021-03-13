from django import forms
from .models import forwards

class forwardQA(forms.ModelForm):
	class Meta:
		model = forwards
		fields = ['name','email']