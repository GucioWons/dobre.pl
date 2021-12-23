from django.db import models

# Create your models here.
from django.urls import reverse


class Rest(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()
    price = models.IntegerField()
    town = models.CharField(max_length=120)
    adres = models.CharField(max_length=120, default="Prosta 1/28")
    cat_id = models.IntegerField(null=False)
    delivery = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('meals-list', kwargs={'my_id':self.id})