from django.contrib import admin
from alpha.models import Doctor, Patient, Appointment, LabTest, Prescription, Bill, Medicine, MedicalRecord


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
class LabtestAdmin(admin.ModelAdmin):
    list_display = ('Test', 'Price', 'Description', 'created_at', 'updated_at',)
    search_fields = ('Test',)
admin.site.register(LabTest, LabtestAdmin)

class Medicineadmin(admin.ModelAdmin):
    list_display = ('id','medicine_name','strength','price','stock','created_at', 'updated_at',)
admin.site.register(Medicine, Medicineadmin)

# Register Prescription Model
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment', 'notes', 'created_at', 'updated_at',)
    search_fields = ('notes',)

admin.site.register(Prescription, PrescriptionAdmin)

class Medicalrecordadmin(admin.ModelAdmin):
    list_display = ( 'id','patient' , 'Appointment','diagnosis' ,'allergies' ,'medical_history','notes','created_at','updated_at' ,)
admin.site.register(MedicalRecord, Medicalrecordadmin)

class Billadmin(admin.ModelAdmin):
    list_display = ('doctor_fee','Appointment','lab_total','medicine_total','discount','tax','grand_total','payment_status','payment_date' , 'created_at', 'updated_at',)
    search_fields = ('lab_total',)

admin.site.register(Bill, Billadmin)

