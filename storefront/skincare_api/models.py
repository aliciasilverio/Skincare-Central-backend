from django.db import models

# Create your models here.
class Contact(models.Model):
    productName = models.CharField(max_length=40)
    image = models.CharField(max_length=500)
    brand = models.CharField(max_length=40)
    price = models.IntegerField()
    benefits = models.CharField(max_length=60)