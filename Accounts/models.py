from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from Meals.models import Meal


class Cart(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    content = models.ManyToManyField(Meal, blank=True)


class Town(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    town = models.CharField(max_length=120, blank=True)
    adres = models.CharField(max_length=120, blank=True)
