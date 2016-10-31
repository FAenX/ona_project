from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage
from geoposition.fields import GeopositionField

# Create your models here.
fs = FileSystemStorage(location='./media/photos')

class Keja(models.Model):	
	_id=models.IntegerField(primary_key=True)
	town=models.CharField(max_length=200,blank=False)
	locality=models.CharField(max_length=200,blank=False)
	rentals_name=models.CharField(max_length=200,blank=False)
	keja_type=models.CharField(max_length=200,blank=False)
	contact_name=models.CharField(max_length=200,blank=False)
	contact_number=models.IntegerField(blank=False)	
	rent=models.IntegerField(blank=False)
	toilet_photo=models.ImageField(storage=fs)
	kitchen_photo=models.ImageField(storage=fs)
	bedroom_photo=models.ImageField(storage=fs)
	_submission_time=models.DateTimeField(blank=False)
	_geolocation=GeopositionField(blank=False)

	






    

	
