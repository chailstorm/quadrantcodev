from django.db import models

# Create your models here.
class contacts(models.Model):
	name = models.CharField(max_length=255,blank=False)
	email = models.CharField(max_length=255,blank=False)
	directed = models.IntegerField(default=0,blank=True)
	comment = models.TextField()