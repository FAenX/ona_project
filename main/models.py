from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage
from geoposition.fields import GeopositionField

# Create your models here.
fs = FileSystemStorage(location='./media/photos')

class Keja(models.Model):	
	_id=models.IntegerField(primary_key=True)
	town=models.CharField(max_length=200,unique=True)
	locality=models.CharField(max_length=200,unique=True)
	rentals_name=models.CharField(max_length=200,unique=True)
	keja_type=models.CharField(max_length=200)
	contact_name=models.CharField(max_length=200)
	contact_number=models.IntegerField()	
	rent=models.IntegerField()
	toilet_photo=models.ImageField(storage=fs)
	kitchen_photo=models.ImageField(storage=fs)
	bedroom_photo=models.ImageField(storage=fs)
	_submission_time=models.DateTimeField()
	_geolocation=GeopositionField()

	def __repr__(self):
		return self._id






    

	
