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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return f"Appointment {self.patient.name} with {self.doctor.name} at {self.date_time}"


class LabTest(models.Model):
    Test = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Discription = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return f"LabTest {self.Test}"