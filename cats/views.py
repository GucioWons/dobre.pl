from django.shortcuts import render, get_object_or_404


# Create your views here.
from Rests.models import Rest
from cats.models import Cat

def rests_list_view(request):
    queryset = Rest.objects.filter(town="Jelenia Góra", cat_id=1)
    obj = get_object_or_404(Cat, id=1)
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