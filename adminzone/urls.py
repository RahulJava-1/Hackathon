from django.urls import re_path
from . import views

app_name="adminzone"

urlpatterns=[
    re_path(r'^adminhome/',views.adminhome,name='adminhome'),
    re_path(r'^patient/',views.patient,name='patient'),
    re_path(r'^doctor/',views.doctor,name='doctor'),
    re_path(r'^addDoc/',views.addDoc,name='addDoc'),
    re_path(r'^docPage/',views.docPage,name='docPage'),
    re_path(r'^deleteDoc/(?P<id>\d+)$',views.deleteDoc,name='deleteDoc'),
    re_path(r'^deletePat/(?P<eid>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.deletePat,name='deletePat'),
    re_path(r'^logout/',views.logout,name="logout"),
]