from django.db import models

# Create your models here.
class avail(models.Model):
	qn = models.IntegerField()
	year = models.IntegerField()
	month = models.IntegerField()
	date = models.IntegerField()
	start = models.CharField(max_length=12)
	end = models.CharField(max_length=12)
	status = models.IntegerField()
	cn = models.IntegerField(null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	meetingid = models.IntegerField(null=True,blank=True)
	joinurl = models.TextField(null=True,blank=True)
	password = models.CharField(max_length=255,null=True,blank=True)
	cost = models.IntegerField(null=True,blank=True)
	orderid = models.CharField(max_length=255,null=True,blank=True)
	qurl = models.TextField(null=True,blank=True)
	curl = models.TextField(null=True,blank=True)
	confirmedEmail = models.IntegerField(default=0)
	canceledEmail = models.IntegerField(default=0)
	
class recur(models.Model):
	days = [('monday','Monday'),('tuesday','Tuesday'),('wednesday','Wednesday'),('thursday','Thursday'),('friday','Friday'),('saturday','Saturday'),('sunday','Sunday')]
	
	qn = models.IntegerField()
	day = models.CharField(max_length=10,choices=days)
	start = models.CharField(max_length=12)
	length = models.IntegerField()