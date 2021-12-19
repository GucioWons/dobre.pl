from django.shortcuts import render, get_object_or_404


# Create your views here.
from Rests.models import Rest
from cats.models import Cat

def rests_list_view(request, my_id):
    queryset = Rest.objects.filter(cat_id=my_id)
    obj = get_object_or_404(Cat, id=my_id)
    context = {
        "object_list": queryset,
        "object": obj
    }
    return render(request, "rests_list.html", context)
def cats_list_view(request):
    queryset = Cat.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "cats_list.html", context)