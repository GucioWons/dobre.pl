from django.db import models

# Create your models here.
from django.urls import reverse


class Cat(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()

    def get_absolute_url(self):
        return reverse('cats:rests-list', kwargs={'my_id':self.id})