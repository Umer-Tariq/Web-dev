from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=5)

class Order(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Item, related_name="orders")