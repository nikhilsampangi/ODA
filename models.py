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

class Hospital_Details(models.Model):
    H_Id = models.CharField(max_length=25)
    H_Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=250)
    Phone1 = models.IntegerField
    Phone2 = models.IntegerField
    Phone3 = models.IntegerField

class Doctor_Type(models.Model):
    T_Id = models.CharField(max_length=100)
    Spec = models.CharField(max_length=250)

class Doctors(models.Model):
    D_Id = models.CharField(max_length=25, primary_key = True)
    H_Id = models.ForeignKey(Hospital_Details, on_delete = models.PROTECT())
    T_Id = models.ForeignKey(Doctor_Type, on_delete = models.PROTECT())
    Avail = models.BooleanField()
    U_N = models.CharField(max_length=25)
    P_W = models.CharField(max_length=25)

class Doctor_Details(models.Model):
    D_Id = models.ForeignKey(Doctors, on_delete = models.PROTECT())
    F_Name = models.CharField(max_length=50)
    L_Name = models.CharField(max_length=50)
    Phone = models.IntegerField
    Degrees = models.CharField(max_length=250)
    Latitudes = models.IntegerField
    Longitudes = models.IntegerField
    Desc = models.TextField
