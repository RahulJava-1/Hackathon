from django.db import models

# Create your models here.
class Register(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    gender=models.CharField(max_length=6)
    contact=models.CharField(max_length=15)
    email=models.EmailField(max_length=50,primary_key=True)
    age=models.IntegerField()
    height=models.CharField(max_length=5)
    aadhar=models.CharField(max_length=30)
    weight=models.CharField(max_length=5)
    password=models.CharField(max_length=15)
    address=models.CharField(max_length=500)
    uniqueID=models.CharField(max_length=6)

class ValidatePatient(models.Model):
    emailID=models.EmailField(max_length=50,primary_key=True)
    password=models.CharField(max_length=15)

class AdminLogin(models.Model):
    adminid=models.EmailField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)

class DoctorLogin(models.Model):
    docId=models.CharField(max_length=10,primary_key=True)
    password=models.CharField(max_length=20)