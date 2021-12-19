from django.db import models

# Create your models here.

class Rest(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    localization = models.CharField(max_length=120)
    cat_id = models.IntegerField(null=False)
    delivery = models.BooleanField(default=True)