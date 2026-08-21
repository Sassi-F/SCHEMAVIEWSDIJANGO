from django.urls import path
from alpha import views

urlpatterns = [
    path('appointments/', views.list_appointments),
]