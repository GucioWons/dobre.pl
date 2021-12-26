from django.urls import path

from Accounts.views import add_to_cart, cart_view, order_create, remove_from_cart

app_name = "accounts"
urlpatterns = [
        path('add-to-cart/<int:my_id>/', add_to_cart, name='add-to-cart'),
        path('remove-from-cart/<int:my_id>/', remove_from_cart, name='remove-from-cart'),
        path('cart/', cart_view, name='cart-view'),
        path('order-create/', order_create, name='order-create'),
    ]
