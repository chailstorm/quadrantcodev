from django.db import models
from django.contrib.auth.models import User
import os


class clientprofile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#activation_key = models.CharField(max_length=255, default=1)
	#email_validated = models.BooleanField(default=False)
	#cn = models.AutoField(primary_key=True)
	position = models.CharField(max_length=255,blank=True)
	company = models.CharField(max_length=255,blank=True)
	location = models.CharField(max_length=255,blank=True)
	
	def __str__(self):
		return self.user.username

		
def path_and_rename(instance, filename):
	ext = filename.split('.')[-1]
	photopath = 'users'
	filename = str(instance.pid)+'.'+ext
	savepath = os.path.join(photopath,filename)
	print(savepath)
	return savepath

class Qphoto(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	pid = models.IntegerField()
	profile_image = models.ImageField(upload_to=path_and_rename)

class Qstripe(models.Model):
	qn = models.IntegerField(primary_key=True)
	acct_id = models.CharField(max_length=255,blank=True)

class QregStr(models.Model):
	code = models.CharField(max_length=255,blank=False)
	status = models.IntegerField(default=0)
	assigned = models.IntegerField(null=True,blank=True)
	
	def __str__(self):
		return str(self.assigned)
	
	
	
