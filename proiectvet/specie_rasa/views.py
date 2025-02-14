from django.http import JsonResponse
from django.shortcuts import render
from specie_rasa.models import Specie, Rasa

# Create your views here.
def specie(request):
    obj = Specie.objects.all()
    data = []

    for specie in obj:
        data.append({"id": specie.id, "nume": specie.nume})

    return JsonResponse(data, safe=False)
            
def rasa(request):
    obj = Rasa.objects.all()
    data = []

    for rasa in obj:
        data.append({"id": rasa.id, "nume": rasa.nume})
        
    return JsonResponse(data, safe=False)