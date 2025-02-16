from django.urls import path
from . import views

urlpatterns = [
    path('specie/', views.specie, name='specie'),
    path('rasa/', views.rasa, name='rasa'),
    path('pacient/', views.pacient, name='pacient'),
    path('consult/', views.consult, name='consult'),
    path('client/', views.client, name='client'),
]