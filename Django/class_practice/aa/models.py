from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=3, decimal_places=1)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)