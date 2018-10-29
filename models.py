from django.db import models

# Create your models here.
class latlng(models.Model):
    lat=models.FloatField()
    lng=models.FloatField()
