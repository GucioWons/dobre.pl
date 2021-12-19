from django.db import models

# Create your models here.

class Cat(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()