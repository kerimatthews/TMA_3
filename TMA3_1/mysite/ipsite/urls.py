from django.urls import path
from . import views
from django.contrib import admin
from ipsite.views import show_ip_address

urlpatterns = [

    path('user_ip/',show_ip_address),
]
