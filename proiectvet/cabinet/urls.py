from django.urls import path
from .views import rasa, specie

urlpatterns = [
    path('specie/', specie.specie, name='specie'),
    path('rasa/', rasa.rasa, name='rasa'),
    path('specie/adauga_rasa/<specie_id>', rasa.adauga_rasa, name='adauga_rasa'),
    path('specie/adauga_specie/', specie.adauga_specie, name='adauga_specie'),
    path('specie/editeaza_specie/<specie_id>', specie.editeaza_specie, name='editeaza_specie'),
    path('specie/sterge_specie/<specie_id>', specie.sterge_specie, name='sterge_specie'),
    path('rasa/editeaza_rasa/<rasa_id>', rasa.editeaza_rasa, name='editeaza_rasa'),
    path('rasa/sterge_rasa/<rasa_id>', rasa.sterge_rasa, name='sterge_rasa'),
]