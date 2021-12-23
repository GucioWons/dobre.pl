from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum

# Create your views here.
from Meals.models import Meal
from Accounts.models import Cart


def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('/landing')
    obj = Cart.objects.get(user=request.user)
    queryset = obj.content.all
    i = list(obj.content.aggregate(Sum('price')).values())[0]
    context = {
        "object_list": queryset,
        "object": obj,
        "sum": float(i)
    }
    return render(request, "cart_view.html", context)

def add_to_cart(request, my_id):
    if not request.user.is_authenticated:
        return redirect('/landing')
    meal=get_object_or_404(Meal, id=my_id)
    cart = Cart.objects.get(user=request.user)
    cart.content.add(meal)
    return redirect("/")
