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

class Blog(models.Model):
    heading = models.CharField(max_length=74)
    image = models.CharField(max_length=300)
    paragraph_1 = models.TextField(max_length=2000, blank=True, null=True)
    paragraph_2 = models.TextField(max_length=2000, blank=True, null=True)
    paragraph_3 = models.TextField(max_length=2000, blank=True, null=True)
    heading_2 = models.CharField(max_length=74, blank=True, null=True)
    image_2 = models.CharField(max_length=200 , blank=True, null=True)   
    paragraph_4 = models.TextField(max_length=2000, blank=True, null=True)
    paragraph_5 = models.TextField(max_length=2000, blank=True, null=True)
    heading_3 = models.CharField(max_length=74, null=True, blank=True)
    image_3 = models.CharField(max_length=300,null=True, blank=True)
    paragraph_6 = models.TextField(max_length=2000, blank=True, null=True)
    tag_1 = models.CharField(max_length=20, blank=True, null=True)
    tag_2 = models.CharField(max_length=20, blank=True, null=True)
    tag_3 = models.CharField(max_length=20, blank=True, null=True)
    tag_4 = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.heading}"