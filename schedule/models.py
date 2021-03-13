from django.db import models

# Create your models here.
class forwards(models.Model):
	qn = models.IntegerField()
	year = models.IntegerField()
	month = models.IntegerField()
	date = models.IntegerField()
	start = models.CharField(max_length=12)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	sent = models.IntegerField(default=0)
	url = models.CharField(max_length = 255)