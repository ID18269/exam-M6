# poets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.poets_list, name='poets_list'),
]
