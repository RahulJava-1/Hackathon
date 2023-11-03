from django.contrib import admin
from . models import Register,ValidatePatient, AdminLogin, DoctorLogin

# Register your models here.
admin.site.register(Register)
admin.site.register(ValidatePatient)
admin.site.register(AdminLogin)
admin.site.register(DoctorLogin)

