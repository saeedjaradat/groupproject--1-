from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('admin_dashboard',views.admin_dash),
    path('login_page',views.login_page),
    path('register_page',views.register_page),
    path('register',views.register),
]