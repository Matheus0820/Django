""" urls alunos """
from django.contrib import admin
from django.urls import path
from .views import home

app_name = 'alunos'

urlpatterns = [
    path('', views.home, name="home")
]