from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum

# Create your views here.
from Rests.models import Meal
from Accounts.models import Cart, Order


def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('/landing')
    obj = Cart.objects.get(user=request.user)
    queryset = obj.content.all
    if obj.content.exists():
        i = list(obj.content.aggregate(Sum('price')).values())[0]
        context = {
            "object_list": queryset,
            "object": obj,
            "sum": float(i)
        }
        return render(request, "cart_view.html", context)
    else:
        context = {
            "object_list": queryset,
            "object": obj,
            "sum": 0
        }
        return render(request, "cart_view.html", context)


def add_to_cart(request, my_id):
    if not request.user.is_authenticated:
        return redirect('/landing')
    meal = get_object_or_404(Meal, id=my_id)
    cart = Cart.objects.get(user=request.user)
    cart.content.add(meal)
    return redirect("/categories")


def remove_from_cart(request, my_id):
    if not request.user.is_authenticated:
        return redirect('/landing')
    meal = get_object_or_404(Meal, id=my_id)
    cart = Cart.objects.get(user=request.user)
    if cart.content.all().contains(meal):
        cart.content.remove(meal)
    return redirect("/cart")


def order_create(request):
    if not request.user.is_authenticated:
        return redirect('/landing')
    cart = Cart.objects.get(user=request.user)
    i = list(cart.content.aggregate(Sum('price')).values())[0]
    order = Order.objects.create(user=request.user, price=float(i))
    order.content.set(cart.content.all())
    cart.content.clear()
    return redirect("/cart")
