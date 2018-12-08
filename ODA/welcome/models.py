from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient_DB(models.Model):
    P_Id = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Age = models.CharField(max_length=3)
    emerg_email = models.CharField(max_length=13,blank=True)
    Gender = models.CharField(max_length=10)
    Blood_group = models.CharField(max_length=5)                                ##changed the max value
    medical_con = models.CharField(max_length=300, default='None')
    image_url = models.CharField(max_length=400, default='')
    user_pat = models.CharField(max_length=4 ,default='no') #############
    Phone_num = models.CharField(max_length=13,blank=True)
    Emergency_num = models.CharField(max_length=50,blank=True)


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
    Phone = models.CharField(max_length=10,blank=True)
    gender = models.CharField(max_length=10, default='Male', blank=True)
    user_pat = models.CharField(max_length=4 ,default='no')      ##############
    doc_type = models.CharField(max_length=250, blank=True)
    Degrees = models.CharField(max_length=250, blank=True)
    d_website = models.CharField(max_length=30, blank=True)
    license = models.CharField(max_length=10,blank=True)
    Latitudes = models.CharField(max_length=50,blank=True, default=0)
    Longitudes = models.CharField(max_length=50,blank=True, default=0)
    About_Clinic = models.TextField(max_length=300,blank=True,default="Its good")
    Desc = models.TextField(blank=True)
    Other_info = models.TextField(max_length=300,blank=True,default="Its great")

    def __str__(self):
        return f'{self.D_Id.username}'