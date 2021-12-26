from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse

from Rests.models import Meal


class Cart(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    content = models.ManyToManyField(Meal, blank=True)


class Town(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    town = models.CharField(max_length=120, blank=True)
    adres = models.CharField(max_length=120, blank=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.ManyToManyField(Meal, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)