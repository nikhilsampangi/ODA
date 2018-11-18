from django.db import models

# Create your models here.
class Disease(models.Model):
    disease_name = models.CharField(max_length=255)
    disease_about = models.TextField()
    disease_causes = models.TextField()
    disease_diagnosis = models.TextField()
    disease_treatment = models.TextField()

    def __self__(self):
        return self.disease_name

class Symptoms(models.Model):
    disease = models.ForeignKey(Disease,on_delete=models.CASCADE)
    symptom = models.TextField()






