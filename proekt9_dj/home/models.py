from django.db import models



class Category(models.Model):
    name=models.CharField(max_length=100)


# Create your models here.
class Products(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=255)


