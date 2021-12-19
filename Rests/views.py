from django.shortcuts import render, get_object_or_404

# Create your views here.

from Meals.models import Meal
from Rests.models import Rest


def meals_list_view(request):
    queryset = Meal.objects.filter(rest_id=1)
    obj = get_object_or_404(Rest, id=1)
    context = {
        "object_list": queryset,
        "object": obj
    }
    return render(request, "meals_list.html", context)
