from django.http import JsonResponse
from django.shortcuts import redirect, render
from cabinet.models.rasa import Rasa, Specie
from cabinet.forms.rasa import AdaugaRasaForm

# Create your views here.

def rasa(request):
    rase = Rasa.objects.all()    
    return render(request, "rasa.html", {"rase": rase})

def adauga_rasa(request, specie_id):
    specie = Specie.objects.get(pk=specie_id)
    if request.method == "POST":
        form = AdaugaRasaForm(request.POST)
        if form.is_valid():
            Rasa.objects.create(nume=form.cleaned_data["nume"], id_specie=specie)
        return redirect("/rasa")
    form = AdaugaRasaForm()
    return render(request, "adauga_rasa.html", {"form": form, "specie": specie})

def editeaza_rasa(request, rasa_id):
    rasa = Rasa.objects.get(id=rasa_id)
    form = AdaugaRasaForm(request.POST or None, instance=rasa)
    if form.is_valid():
        form.save()
        return redirect("/rasa")
    return render(request, "editeaza.html", {"form": form})

def sterge_rasa(request, rasa_id):
    rasa = Rasa.objects.get(pk=rasa_id)
    rasa.delete()
    return redirect("/rasa")