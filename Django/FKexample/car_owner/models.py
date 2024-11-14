from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

class Car(models.Model):
    company = models.CharField(max_length=200)
    year = models.IntegerField()
    owner = models.ForeignKey(Owner, related_name="cars", on_delete=models.CASCADE)