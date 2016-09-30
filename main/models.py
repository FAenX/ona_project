from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Keja(models.Model):
	ona_object_id=models.IntegerField(primary_key=True)
	town=models.CharField(max_length=200,unique=True)
	locality=models.CharField(max_length=200,unique=True)
	name=models.CharField(max_length=200,unique=True)
	kejatype=models.CharField(max_length=200)
	caretaker=models.CharField(max_length=200)
	caretaker_no=models.IntegerField()	
	rent=models.IntegerField()
	toilet_photo=models.ImageField(upload_to='project_images')
	kitchen_photo=models.ImageField(upload_to='project_images')
	bedroom_photo=models.ImageField(upload_to='project_images')
	pub_date=models.DateTimeField(upload_to='project_images')

	
