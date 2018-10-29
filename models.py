from django.db import models

# Create your models here.
class latlng(models.Model):
    lat=models.FloatField()
    lng=models.FloatField()
    
# patients database

class Patient_DB(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.IntegerField
    Gender = models.CharField(max_length=10)
    Blood_group = models.CharField(max_length=3)
    Maritial_Status = models.CharField(max_length=3)
    Phone_num = models.IntegerField
    Emergency_num = models.IntegerField
    PatientId = models.CharField(max_length=255, default='0')
    Email_Id = models.CharField(max_length=255,default='NULL')
