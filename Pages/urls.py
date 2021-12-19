from django.urls import path

from Pages.views import register_page, logout_view, login_page

app_name = "pages"
urlpatterns = [
        path('register/', register_page, name='user-register'),
        path('logout/', logout_view, name='user-logout'),
        path('login/', login_page, name='user-login')
    ]
