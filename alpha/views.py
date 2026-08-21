from django.shortcuts import render

from alpha.models import Appointment


# Create your views here.

def list_appointments(request):
    print("list appointments view is called...")

    appointments = Appointment.objects.all()
    print(appointments)
    for a in appointments:
        print(a)
    context = {
        'appointments': appointments
    }

    return render(request, "appointments.html", context=context)