from django.db import models
from django import forms
from datetime import datetime


GENDER = (
			('m','M'),
		    ('f','F')
		)

STATUS = (
			('available','AVAILABLE'),
			('filled','FILLED')
		 )
TYPE = (
			('S','SINGLE'),
			('D','DOUBLE'),
			('S/AC','SINGLE(AC)'),
			('D/AC','DOUBLE(AC)')
		)

# Create your models here.
class patient(models.Model):
	pid = models.AutoField(primary_key=True)
	patient_name = models.CharField(max_length=200)
	age = models.IntegerField()
	gender = models.CharField(max_length=5, choices=GENDER)
	weight = models.IntegerField()
	address = models.TextField()
	phone_no = models.CharField(max_length=15)
	disease = models.TextField()
	doctorid = models.CharField(max_length=10)



	def __str__(self):
		return self.patient_name

class doctor(models.Model):
	doctorid = models.AutoField(primary_key=True)
	doctor_name = models.CharField(max_length=25)
	dept = models.CharField(max_length=30)


	def __str__(self):
		return self.doctor_name

class lab(models.Model):
	labid = models.AutoField(primary_key=True)
	pid = models.ForeignKey('patient', on_delete=models.CASCADE)
	date = models.DateTimeField(default=datetime.now())
	category = models.CharField(max_length=30)
	amount = models.IntegerField()


	def __str__(self):
		return self.labid


class patientInfo(models.Model):
	pid = models.ForeignKey('patient', on_delete=models.CASCADE, null=True)
	room_no = models.ForeignKey('roomInfo', on_delete=models.CASCADE)
	name = models.CharField(default="NONAME", max_length=20)
	date_of_admn = models.DateTimeField(default=datetime.now())
	date_of_dis = models.DateTimeField(null=True)
	advance_amt = models.IntegerField(default=800)


	def __str__(self):
		return self.name




class roomInfo(models.Model):
	room_no = models.CharField(max_length=5, primary_key=True)
	room_type = models.CharField(max_length=10, choices=TYPE)
	available = models.BooleanField(default=True)


	def __str__(self):
		return self.room_no


class billInfo(models.Model):
	bill_no = models.CharField(max_length=10, primary_key=True)
	pid = models.ForeignKey('patient', on_delete=models.CASCADE)
	doc_charge = models.IntegerField()
	med_charge = models.IntegerField()
	room_charge = models.IntegerField()
	surgery_charge = models.IntegerField()
	no_of_days = models.IntegerField()
	nursing_charge = models.IntegerField()
	labid = models.ForeignKey('lab', on_delete=models.CASCADE)
	net_amt = models.IntegerField()

	def __str__(self):
		return sel.bill_no