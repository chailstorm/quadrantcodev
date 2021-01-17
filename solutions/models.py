from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class qinfo(models.Model):
	prefixes = (('Mr.','Mr.'),('Mrs.','Mrs.'),('Ms.','Ms.'),('Dr.','Dr.'),)
	suffixes = (('PhD','PhD'),('M.D.','M.D.'),)
	categories = (('medicine','Medicine'),)
	actives = ((1,'Yes'),(0,'No'),)
	competency = ((1,'Yes'),(0,'No'))
	
	#qn = models.AutoField(primary_key=True)
	#user = models.OneToOneField(User, on_delete=models.CASCADE) #DONT TURN THIS ON IT WILL BREAK THE MODEL
	qn = models.IntegerField(primary_key=True)
	active = models.IntegerField(choices=actives,default=1)
	prefix = models.CharField(max_length=255,choices=prefixes,blank=True)
	first = models.CharField(max_length=255)
	last = models.CharField(max_length=255)
	suffix = models.CharField(max_length=255,choices=suffixes,blank=True)
	category = models.CharField(max_length=255,choices=categories)
	servicelinedev = models.IntegerField(choices=competency,default=0)
	capitalplan = models.IntegerField(choices=competency,default=0)
	pysicianrecruitment = models.IntegerField(choices=competency,default=0)
	processimprove = models.IntegerField(choices=competency,default=0)
	productivity = models.IntegerField(choices=competency,default=0)
	operationsfinance = models.IntegerField(choices=competency,default=0)
	leadingmeetings = models.IntegerField(choices=competency,default=0)
	dataanalysis = models.IntegerField(choices=competency,default=0)
	teamcourses = models.IntegerField(choices=competency,default=0)
	personalleadership = models.IntegerField(choices=competency,default=0)
	personalitytypes = models.IntegerField(choices=competency,default=0)
	tempassignments = models.IntegerField(choices=competency,default=0)
	special1 = models.CharField(max_length=255,blank=False)
	special2 = models.CharField(max_length=255,blank=False)
	special3 = models.CharField(max_length=255,blank=False)
	special4 = models.CharField(max_length=255,blank=False)
	special5 = models.CharField(max_length=255,blank=False)
	description = models.CharField(max_length=255,blank=False)
	bio = models.TextField()
	linkedin = models.CharField(max_length=255,null=True,blank=True)
	yearexp = models.IntegerField(blank=False)
	email = models.CharField(max_length=255,blank=False,default='example@gmail.com')
	cost = models.IntegerField(default=100)
	
	#def __str__(self):
	#	return str(self.qn)
	
	def get_absolute_url(self):
		return reverse('q',args=[str(self.qn)])
		
	def __str__(self):
		#fullnamestr = self.prefix + '' + self.first + '' + self.last + '' + self.suffix
		return f'{self.prefix} {self.first} {self.last} {self.suffix}'
