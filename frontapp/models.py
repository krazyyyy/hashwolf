from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    url = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=500,blank=True, null=True)
    image = models.CharField(blank=True, null=True, max_length=500)
    category = models.CharField(blank=True, null=True, max_length=500)
    brand = models.CharField(blank=True, null=True, max_length=500)



    def __str__(self):
        return f"{self.name} for {self.price}"