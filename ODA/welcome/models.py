from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor_Type(models.Model):
    T_Id = models.CharField(max_length=100)
    Spec = models.CharField(max_length=250)

class Hospital_Details(models.Model):
    H_Id = models.OneToOneField(User, on_delete=models.CASCADE)
    H_Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=250)
    Phone1 = models.IntegerField(null=True)

class Doctors(models.Model):
    D_Id = models.OneToOneField(User, on_delete=models.CASCADE ,primary_key=True)
    H_Id = models.ForeignKey(Hospital_Details, on_delete=models.PROTECT, null=True)
    T_Id = models.ForeignKey(Doctor_Type, on_delete=models.PROTECT, null=True)
    Avail = models.BooleanField(blank=True ,default=True )
    Phone = models.CharField(max_length=13,blank=True)
    gender = models.CharField(max_length=10, default='Male', blank=True)
    Degrees = models.CharField(max_length=250, blank=True)
    license = models.CharField(max_length=10,blank=True)
    Latitudes = models.IntegerField(blank=True, default=0)
    Longitudes = models.IntegerField(blank=True, default=0)
    Desc = models.TextField(blank=True)

    def __str__(self):
        return f'{self.D_Id.username}'