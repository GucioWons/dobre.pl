from django.urls import path

from cats.views import rests_list_view, cats_list_view

app_name = "cats"
urlpatterns = [
        path('categories/', cats_list_view, name='cats-list'),
        path('category/<int:my_id>/', rests_list_view, name='rests-list'),
    ]
