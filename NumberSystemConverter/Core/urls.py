from django.urls import path
from . import views

urlpatterns = [
    path('', views.Core, name = 'Core'),
]
