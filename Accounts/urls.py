from django.urls import path

from Accounts.views import add_to_cart, cart_view

app_name = "accounts"
urlpatterns = [
        path('add-to-cart/<int:my_id>/', add_to_cart, name='add-to-cart'),
        path('cart/', cart_view, name='cart-view'),
    ]
