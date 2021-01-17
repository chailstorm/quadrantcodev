from django.db import models
#from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class post(models.Model):
	bn = models.AutoField(primary_key=True)
	statuses = ((1,'Published'),(0,'Hidden'))
	
	title = models.CharField(max_length=255)
	status = models.IntegerField(choices=statuses)
	author = models.IntegerField()
	name = models.CharField(max_length=255)
	body = RichTextUploadingField(blank=True,null=True)
	post_date = models.DateField(auto_now_add=True)
	
	class Meta:
		ordering = ['-post_date']

class comment(models.Model):
	statuses = ((1,'Published'),(0,'Hidden'))
	bcn = models.AutoField(primary_key=True)
	bn = models.IntegerField()
	status = models.IntegerField(choices=statuses)
	author = models.IntegerField()
	name = models.CharField(max_length=255)
	body = RichTextField(blank=True,null=True)
	post_date = models.DateField(auto_now_add=True)
	
	class Meta:
		ordering = ['-post_date']
	