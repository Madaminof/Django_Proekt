from django.db import models



class Category(models.Model):
    name=models.CharField(max_length=100)


# Create your models here.
class Hayvonlar(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField()
 