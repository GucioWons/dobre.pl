from django.urls import path

from Rests.views import rests_list_view, cats_list_view

app_name = "rests"
urlpatterns = [
        path('categories/', cats_list_view, name='cats-list'),
        path('category/<int:my_id>/', rests_list_view, name='rests-list'),
    ]
