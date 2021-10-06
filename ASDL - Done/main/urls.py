from . import views
from django.urls import path,include

app_name = "main"

urlpatterns = [
	path("", views.homepage, name="homepage"),
    path("subhome2/",views.subhome,name='subhome'), 
   
	path("register/",views.register,name="register"),
    path('', include('django.contrib.auth.urls')),
	path("login/", views.login_request, name="login"), 
    path("preg/",views.AddPatient,name='patient_register'),  
    path("pinfobase/",views.PatientInfo,name='patient_info'),
    path("search/",views.search,name='search'),  
    path("roombase/",views.RoomBase,name='room_base'),
    path('room/',views.BookRoom,name='room_book'),
    path('RoomFilled/',views.RoomFilled,name='RoomFilled'),
    path('RoomCancel/',views.RoomCancel,name='RoomCancel'),
    path('RoomSearch/',views.RoomSearch,name='RoomSearch'),
    path('RoomSearchInfo/',views.RoomSearchInfo,name='RoomSearchInfo'),
    path('Discharge/',views.Discharge,name='Discharge'),
    path('DischargeInfo/',views.DischargeInfo,name='DischargeInfo'),










]

