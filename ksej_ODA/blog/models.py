from django.db import models
from django.contrib.auth.models import User


# patients database

class Patient_DB(models.Model):
    P_Id = models.OneToOneField(User, on_delete=models.CASCADE)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Blood_group = models.CharField(max_length=3)
    Marital_Status = models.CharField(max_length=3)
    Phone_num = models.IntegerField()
    Emergency_num = models.IntegerField()


class Hospital_Details(models.Model):
    H_Id = models.OneToOneField(User, on_delete=models.CASCADE)
    H_Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=250)
    Phone1 = models.IntegerField()
    Phone2 = models.IntegerField()
    Phone3 = models.IntegerField()


class Doctor_Type(models.Model):
    T_Id = models.CharField(max_length=100)
    Spec = models.CharField(max_length=250)


class Doctors(models.Model):
    D_Id = models.OneToOneField(User, on_delete=models.CASCADE)
    H_Id = models.ForeignKey(Hospital_Details, on_delete=models.PROTECT)
    T_Id = models.ForeignKey(Doctor_Type, on_delete=models.PROTECT)
    Avail = models.BooleanField(blank=True)
    Phone = models.IntegerField(blank=True, default=0)
    Degrees = models.CharField(max_length=250, blank=True)
    Latitudes = models.IntegerField(blank=True, default=0)
    Longitudes = models.IntegerField(blank=True, default=0)
    Desc = models.TextField(blank=True)


class textinblog(models.Model):
    doctors = models.ForeignKey(Doctors, on_delete=models.PROTECT)
    the_text = models.TextField()
    the_sub = models.CharField(default='None', null=True, max_length=150)

    # def __str__(self):
    #     return self.the_text


class Tips(models.Model):
    tip = models.TextField()


class Medical_shop(models.Model):
    shop_id = models.CharField(max_length=255, primary_key=True)
    shop_name = models.CharField(max_length=255)
    Lattitude = models.FloatField(default='NULL')
    Longitude = models.FloatField(default='NULL')


class Stock_availability(models.Model):
    shop_id = models.ForeignKey(Medical_shop, on_delete=models.PROTECT)
    Med_id = models.CharField(max_length=255)
    Medicine_name = models.CharField(max_length=255)
    Stock = models.IntegerField()


class General_Medicine(models.Model):
    Disease = models.CharField(max_length=255, primary_key=True)
    Medicine = models.CharField(max_length=255)


class Blood_Bank(models.Model):
    BB_id = models.CharField(max_length=255, primary_key=True)
    BB_name = models.CharField(max_length=255)
    Lat = models.FloatField(default='NULL')
    Long = models.FloatField(default='NULL')


class Blood_avail(models.Model):
    BB_id = models.ForeignKey(Blood_Bank, on_delete=models.PROTECT)
    Blood_grp = models.CharField(max_length=255)
    Availability = models.CharField(max_length=255)
