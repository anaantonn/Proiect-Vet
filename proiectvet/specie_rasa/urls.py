from django.urls import path
from . import views

urlpatterns = [
    path('specie/', views.specie, name='specie'),
    path('rasa/', views.rasa, name='rasa'),
]