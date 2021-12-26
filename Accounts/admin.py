from django.contrib import admin

# Register your models here.
from Accounts.models import Cart, Town, Order

admin.site.register(Cart)
admin.site.register(Town)
admin.site.register(Order)
