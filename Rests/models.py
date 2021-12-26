from django.db import models

# Create your models here.
from django.urls import reverse


class Cat(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True)

    def get_absolute_url(self):
        return reverse('rests:rests-list', kwargs={'my_id': self.id})


class Rest(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()
    price = models.IntegerField()
    town = models.CharField(max_length=120)
    adres = models.CharField(max_length=120, default="Prosta 1/28")
    category = models.ForeignKey(Cat, null=False, on_delete=models.CASCADE)
    delivery = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('meals-list', kwargs={'my_id': self.id})


class Meal(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    restaurant = models.ForeignKey(Rest, null=False, on_delete=models.CASCADE)
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('rests:rests-list', kwargs={'my_id': self.id})

    def get_add_to_cart_url(self):
        return reverse('accounts:add-to-cart', kwargs={'my_id': self.id})

    def get_remove_from_cart_url(self):
        return reverse('accounts:remove-from-cart', kwargs={'my_id': self.id})
