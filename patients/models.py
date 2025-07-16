from django.db import models


disease = [
    ("yes", "YES"),
    ("No", "NO"),
]

class Patient(models.Model):


    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    phone = models.IntegerField()
    address = models.TextField(max_length=500,default="NULL")
    diagnosis = models.CharField(max_length=255)
    speciall_disease = models.CharField(max_length=3,choices= disease,default="NO")
    Medical_Problems = models.TextField(max_length=700,default="NULL")

    def __str__(self):
        return self.name