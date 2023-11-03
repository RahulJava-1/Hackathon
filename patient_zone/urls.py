from django.urls import path
from . import views

app_name="patient_zone"

urlpatterns=[
    path('phome/',views.phome,name='phome'),
    path('logout/',views.logout,name='logout'),
]