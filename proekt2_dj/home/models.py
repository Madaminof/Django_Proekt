from django.db import models


# Create your models here.
class Cars(models.Model):
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=255)




class Category(models.Model):
    name=models.CharField(max_length=100)

