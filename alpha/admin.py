from django.contrib import admin
from alpha.models import Doctor, Patient, Appointment, LabTest


# Register Doctor Model
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'email', 'phone', 'consultation_fees', 'created_at', 'updated_at')
    list_filter = ('specialization', 'consultation_fees')
    search_fields = ('name',)
admin.site.register(Doctor, DoctorAdmin)


# Register Patient Model
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'dob', 'email', 'address', 'blood_group', 'created_at', 'updated_at')
    list_filter = ('blood_group', 'gender')
    search_fields = ('name',)
admin.site.register(Patient, PatientAdmin)


# Register Appointment Model
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'remarks', 'status', 'created_at', 'updated_at')
admin.site.register(Appointment, AppointmentAdmin)

# Register Appointment Model
class labtestAdmin(admin.ModelAdmin):
    list_display = ('Test', 'Price', 'Discription', 'created_at', 'updated_at')
    search_fields = ('Test', 'Price', 'Discription', 'created_at', 'updated_at')
admin.site.register(LabTest, labtestAdmin)
