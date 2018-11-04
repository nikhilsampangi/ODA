from django.db import models


# Create your models here.
class latlng(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()


# patients database

class Patient_DB(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Blood_group = models.CharField(max_length=3)
    medical_con = models.CharField(max_length=255,default="No Problems")
    Phone_num = models.CharField(max_length=13)
    Emergency_num = models.CharField(max_length=13)
    PatientId = models.CharField(max_length=255, default='0')
    Email_Id = models.CharField(max_length=255, default='NULL')



class Tips(models.Model):
    tip = models.TextField()

