from django.db import models

# Create your models here.
class AddDoc(models.Model):
    name = models.CharField(max_length=50)
    contact=models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    docId = models.CharField(max_length=10,primary_key=True)
    password=models.CharField(max_length=10)