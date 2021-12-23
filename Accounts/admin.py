from django.contrib import admin

# Register your models here.
from Accounts.models import Cart, Town

admin.site.register(Cart)
admin.site.register(Town)
