from django.db import models

# Create your models here.
class cardetails(models.Model):
	FUEL_TYPE =[
		('Diesel','Diesel'),
		('Petrol','Petrol'),
		('CNG','CNG'),
		('LPG','LPG'),
	]
	TRANSMISSION = [
		('Automatic','Automatic'),
		('Manual','Manual')
	]
	OWNER_TYPE = [
		('First','First owner of car'),
		('Second','Second owner of car'),
		('Third','Third owner'),
		('Fourth & Above','Fourth & Above')
	]
	Model_car=models.CharField(max_length=64)
	location=models.CharField(max_length=15)
	year=models.PositiveIntegerField()
	KM_driven=models.PositiveIntegerField()
	fuel_type=models.CharField(max_length=10,choices=FUEL_TYPE)
	transmission=models.CharField(max_length=16,choices=TRANSMISSION)
	owner_type=models.CharField(max_length=16,choices=OWNER_TYPE)
	mileage=models.FloatField()
	engine=models.PositiveIntegerField()
	power=models.FloatField()
	seats=models.PositiveSmallIntegerField()
	bought_at=models.PositiveIntegerField()

	def __str__(self):
		return self.name