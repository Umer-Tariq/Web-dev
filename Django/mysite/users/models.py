from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=75)
    password = models.CharField(max_length=75)

    def __str__(self) -> str:
        return self.username