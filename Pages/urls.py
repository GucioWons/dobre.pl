from django.urls import path

from Pages.views import register_page, logout_view, login_page, settings_page, landing_page

app_name = "pages"
urlpatterns = [
        path('register/', register_page, name='user-register'),
        path('logout/', logout_view, name='user-logout'),
        path('login/', login_page, name='user-login'),
        path('settings/', settings_page, name='user-settings'),
        path('landing/', landing_page, name='landing_page')
    ]
