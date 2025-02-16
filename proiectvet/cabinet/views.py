from django.http import JsonResponse
from django.shortcuts import render
from cabinet.models import Client, Consult, Pacient, Rasa, Specie

# Create your views here.

def client(request):
    obj = Client.objects.all()
    data = []

    for client in obj:
        data.append({"id": client.id, "nume": client.nume,
                     "prenume": client.prenume,
                     "telefon": client.telefon,
                     "email": client.email})
        
    return JsonResponse(data, safe=False)

def consult(request):
    obj = Consult.objects.all()
    data = []

    for consult in obj:
        data.append({"id": consult.id, "data": consult.data,
                     "anamneza": consult.anamneza,
                     "temperatura": consult.temperatura,
                     "greutate": consult.greutate,
                     "heart_rate": consult.heart_rate,
                     "respiratory_rate": consult.respiratory_rate,
                     "observatii": consult.observatii})
        
    return JsonResponse(data, safe=False)

def pacient(request):
    obj = Pacient.objects.all()
    data = []

    for pacient in obj:
        data.append({"id": pacient.id, "nume": pacient.nume,
                     "sex": pacient.sex, 
                     "data_nastere": pacient.data_nastere})
        
    return JsonResponse(data, safe=False)

def rasa(request):
    obj = Rasa.objects.all()
    data = []

    for rasa in obj:
        data.append({"id": rasa.id, "nume": rasa.nume})
        
    return JsonResponse(data, safe=False)

def specie(request):
    obj = Specie.objects.all()
    data = []

    for specie in obj:
        data.append({"id": specie.id, "nume": specie.nume})

    return JsonResponse(data, safe=False)