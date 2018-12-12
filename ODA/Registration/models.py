from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

class Medical(models.Model):
    shop_id = models.CharField(max_length=255,primary_key = True)
    shop_name = models.CharField(max_length=255)
    Lattitude = models.FloatField(default=0)
    Longitude = models.FloatField(default=0)


class Stock(models.Model):
    shop_id = models.ForeignKey(Medical,on_delete=models.PROTECT)
    Med_id = models.CharField(max_length=255)
    Medicine_name = models.CharField(max_length=255)
    Stock = models.IntegerField()
