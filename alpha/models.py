from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255)
    consultation_fees = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Dr {self.name}"

class Patient(models.Model):
    name = models.CharField(max_length=255)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default='M')
    dob = models.DateField()
    email = models.EmailField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Patient {self.name}"

class LabTest(models.Model):
    Test = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"LabTest {self.Test}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    remarks = models.TextField(null=True, blank=True)
    APPOINTMENT_STATUS_CHOICES = [
        ("Completed", "Completed"),
        ("Pending", "Pending"),
        ("Cancelled", "Cancelled"),
    ]
    status = models.CharField(max_length=255, choices=APPOINTMENT_STATUS_CHOICES)
    lab_tests = models.ManyToManyField(LabTest)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Status {self.status}"

class Medicine(models.Model):
    id= models.AutoField(primary_key=True)
    medicine_name = models.CharField(max_length=255)
    strength = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Medicine {self.medicine_name}"

class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    medicine = models.ManyToManyField(Medicine)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.id}"

class MedicalRecord(models.Model):
    id= models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    diagnosis = models.TextField(null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.id}"

class Bill(models.Model):
    doctor_fee= models.DecimalField(max_digits=6, decimal_places=2)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True)
    lab_test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
    lab_total = models.DecimalField(max_digits=6, decimal_places=2)
    medicine = models.DecimalField(max_digits=6, decimal_places=2)
    medicine_total = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(max_digits=6, decimal_places=2)
    tax= models.DecimalField(max_digits=6, decimal_places=2)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2)
    PAYMENT_STATUS_CHOICES = [
        ("P", "Paid"),
        ("u", "Unpaid"),
    ]
    payment_status = models.CharField(max_length=6, choices=PAYMENT_STATUS_CHOICES)
    payment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"
