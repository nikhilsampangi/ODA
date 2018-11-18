from django.db import models

# Create your models here.
class Medical_shop (models.Model):
    shop_id = models.CharField(max_length=255,primary_key = True)
    shop_name = models.CharField(max_length=255)
    Lattitude = models.FloatField(default='NULL')
    Longitude = models.FloatField(default='NULL')

class Stock_availability (models.Model):
    shop_id = models.ForeignKey(Medical_shop,on_delete=models.PROTECT)
    Med_id = models.CharField(max_length=255)
    Medicine_name = models.CharField(max_length=255)
    Stock = models.IntegerField()

class General_Medicine(models.Model):
    Disease = models.CharField(max_length=255,primary_key = True)
    Medicine = models.CharField(max_length=255)

class Blood_Bank(models.Model):
    BB_id=models.CharField(max_length=255,primary_key=True)
    BB_name=models.CharField(max_length=255)
    Lat = models.FloatField(default='NULL')
    Long = models.FloatField(default='NULL')

class Blood_avail(models.Model):
    BB_id=models.ForeignKey(Blood_Bank,on_delete=models.PROTECT)
    Blood_grp=models.CharField(max_length=255)
    Availability=models.CharField(max_length=255)