from django.urls import path
from apps.inicio import views

urlpatterns = [
    path('', views.home, name='home')
]