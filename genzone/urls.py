from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('registration',views.registration,name="registration"),
    path('cardio',views.cardio, name="cardio"),
    path('gastro',views.gastro, name="gastro"),
    path('neuro',views.neuro, name="neuro"),
    path('ortho',views.ortho, name="ortho"),
    path('patientLogin',views.patientLogin,name="patientLogin"),
    path('vPatient',views.vPatient,name="vPatient"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('vAdmin',views.vAdmin,name="vAdmin"),
    path('doctorlogin',views.doctorlogin,name='doctorlogin'),
    path('vDoctor/',views.vDoctor,name='vDoctor'),
    path('regSignup/',views.regSignup,name="regSignup"),
    path('unique/',views.unique,name="unique"),
]