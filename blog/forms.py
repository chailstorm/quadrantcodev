from django import forms
from .models import post, comment

class blogposts(forms.ModelForm):
	class Meta:
		model = post
		fields = ['title','body']

class commentposts(forms.ModelForm):
	class Meta:
		model = comment
		fields = ['body']