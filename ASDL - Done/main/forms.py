from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django import forms
from django.contrib.auth.models import User 
from .models import patient, patientInfo


GENDER = (
			('m','M'),
		    ('f','F')
		)


class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

class AuthForm(AuthenticationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["email","username", "password1"]

class PatientForm(forms.ModelForm):

	class Meta:
		model = patient
		fields = ["pid", "patient_name", "age", "gender", "weight", "address", "phone_no", "disease", "doctorid"]

		widgets = {

			'pid' : forms.TextInput(attrs={'class': 'form-control'}),
			'patient_name' : forms.TextInput(attrs={'class': 'form-control'}),
			'age' : forms.TextInput(attrs={'class': 'form-control'}),
			'gender' : forms.TextInput(attrs={'class': 'form-control'}),			
			'weight' : forms.TextInput(attrs={'class': 'form-control'}),
			'address' : forms.Textarea(attrs={'class': 'form-control'}),
			'phone_no' : forms.TextInput(attrs={'class': 'form-control'}),
			'disease' : forms.TextInput(attrs={'class': 'form-control'}),
			'doctorid' : forms.TextInput(attrs={'class': 'form-control'}),
		}


class BookingForm(forms.ModelForm):
	
	class Meta:
		model = patientInfo
		fields = ["pid","name","room_no","date_of_admn","advance_amt"]

		widgets = {

				'pid' : forms.TextInput(attrs={'class': 'form-control'}),
				'name' : forms.TextInput(attrs={'class': 'form-control'}),
				'room_no' : forms.TextInput(attrs={'class': 'form-control'}),
				'date_of_admn' : forms.TextInput(attrs={'class': 'form-control'}),
				'advance_amt' : forms.TextInput(attrs={'class': 'form-control'}),

				}


class DischargeForm(forms.ModelForm):

	class Meta:
		model = patientInfo
		fields = ["date_of_dis"]

		widgets = {
				'date_of_dis' : forms.TextInput(attrs={'class': 'form-control'}),
				  }	