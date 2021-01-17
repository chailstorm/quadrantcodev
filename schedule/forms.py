from django import forms

class forwardQA(forms.Form):
	name = forms.CharField(max_length=255)
	email = forms.CharField(max_length=255)