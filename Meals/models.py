from django.db import models

# Create your models here.
from django.urls import reverse

class Meal(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    rest_id = models.IntegerField(null=False)
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('products:product-detail', kwargs={'id':self.id})