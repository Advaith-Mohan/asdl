from django.contrib import admin
from .models import patient, doctor, lab, patientInfo, roomInfo, billInfo
# Register your models here.
admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(lab)
admin.site.register(patientInfo)
admin.site.register(roomInfo)
admin.site.register(billInfo)