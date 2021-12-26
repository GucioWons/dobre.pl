from django.contrib import admin

# Register your models here.
from Rests.models import Rest, Meal, Cat

admin.site.register(Rest)
admin.site.register(Meal)
admin.site.register(Cat)
