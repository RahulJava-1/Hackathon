from django.urls import path
from . import views

app_name="doctor_zone"

urlpatterns=[
    path('docHome',views.docHome,name='docHome'),
    path('logout/',views.logout,name='logout'),
]