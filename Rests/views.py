from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from Meals.models import Meal
from Rests.models import Rest


def meals_list_view(request, my_id):
    if not request.user.is_authenticated:
        return redirect('/landing')
    queryset = Meal.objects.filter(rest_id=my_id)
    obj = get_object_or_404(Rest, id=my_id)
    context = {
        "object_list": queryset,
        "object": obj
    }
    return render(request, "meals_list.html", context)
