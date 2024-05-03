from django.db import models
from django.db.models import CharField


# Create your models here.


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'category'

    def __str__(self) -> CharField:
        return self.name


class Phone(models.Model):
    objects = None
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    model = models.CharField(max_length=150)
    make = models.CharField(max_length=150)
    body = models.TextField()
    price = models.IntegerField()

    class Meta:
        db_table = 'products'

    def __str__(self) -> str:
        return f"{self.category.name}  {self.model}"




