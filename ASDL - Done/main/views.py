from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from .forms import RegisterForm, AuthForm, PatientForm, BookingForm, DischargeForm
from .models import patient, roomInfo, patientInfo
from datetime import datetime



# main homepage
def homepage(request):
	return render(request=request,
				  template_name="main/homebs.html",
				  )

# sub homepage
def subhome(request):
	return render(request=request,
				  template_name="main/subhome2.html",
				  )





# registering new user
def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/")
			
	else:
		form = RegisterForm()


	return render(request,
				  "main/register.html",
				  context={"form":form})


# user login
def login_request(request):
	if request.user.is_authenticated:
		messages.add_message(request, messages.INFO, 'You are already Logged in.')
		return HttpResponseRedirect('/preg')
	else:
		form = AuthForm()
		return render(request,
				  	"main/login.html",
				  	{"form":form})

#user logout
@login_required
def logout_request(request):
	logout(request)
	messages.info(request, "Logged Out Successfully!!!!")
	return  redirect("main:homepage")


#adding new patients
@login_required
def AddPatient(response):
	form = PatientForm()
	if response.method == "POST":
		form = PatientForm(response.POST)
		if form.is_valid():
			form.save()
			messages.info(response, "Saved")
			return redirect("main:subhome")
		
	else:
		form = PatientForm()
		
	
	return render(response,
				  "main/preg.html",
				  {"form":form})


#searchng for patient
@login_required
def PatientInfo(request):
	return render(request=request,
				  template_name="main/pinfobase.html",
				  )


#patient search result
def search(request):
	query = request.GET['query']
	pat = patient.objects.filter(patient_name__icontains=query)
	params = {'pat':pat}
	return render(request,"main/pinfo.html",params)


#searching rooms for booking
def RoomBase(request):
	return render(request=request,
				  template_name="main/roombase.html",
				  )


#option to book
def BookRoom(request):
	q = request.GET['q']
	rm =  roomInfo.objects.filter(room_type__icontains=q)
	p = {'rm':rm}
	return render(request,"main/room.html",p)


#booking room
def RoomFilled(request):
	x = get_object_or_404(roomInfo, pk=request.GET.get('x_id'))
	form = BookingForm()
	if request.method == "POST":
		form = BookingForm(request.POST)
		if form.is_valid():
			x.available = False
			x.save()
			form.save()
			return redirect("main:room_base")
		
	else:
		form = BookingForm()
	
	return render(request,
				  "main/book.html",
				  {"form":form})


#cancelling room
def RoomCancel(request):
	x = get_object_or_404(roomInfo, room_no=request.GET.get('rno'))
	y = get_object_or_404(patientInfo, room_no=request.GET.get('rno'))
	y.date_of_dis = datetime.now()
	y.save()
	print(y.date_of_dis)
	x.available = True
	x.save()
	return redirect("main:subhome")

#searching for patient room
def RoomSearch(request):
	return render(request=request,
				  template_name="main/roomsearch.html",
				  )


#room search results
def RoomSearchInfo(request):
	room = request.GET['room']
	rs =  patientInfo.objects.filter(name__icontains=room)
	s = {'rs':rs}
	return render(request,"main/roomsearchinfo.html",s)



def Discharge(request):
	return render(request=request,
				  template_name="main/pdisbase.html",
				  )


def DischargeInfo(request):
	dis = request.GET['dis']
	rd =  patientInfo.objects.filter(name__icontains=dis)
	d = {'rd':rd}
	return render(request,"main/pdisinfo.html",d)








