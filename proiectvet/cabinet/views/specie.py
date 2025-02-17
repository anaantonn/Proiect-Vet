from django.http import JsonResponse
from django.shortcuts import redirect, render
from cabinet.models.specie import Specie
from cabinet.forms.specie import AdaugaSpecieForm

# Create your views here.

def specie(request):
    specii = Specie.objects.all()    
    return render(request, "specie.html", {"specii": specii})

def adauga_specie(request):
    if request.method == "POST":
        form = AdaugaSpecieForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/specie")
    return render(request, "adauga_specie.html", {"form": AdaugaSpecieForm})

def editeaza_specie(request, specie_id):
    specie = Specie.objects.get(id=specie_id)
    form = AdaugaSpecieForm(request.POST or None, instance=specie)
    if form.is_valid():
        form.save()
        return redirect("/specie")
    return render(request, "editeaza.html", {"form": form})

def sterge_specie(request, specie_id):
    specie = Specie.objects.get(pk=specie_id)
    specie.delete()
    return redirect("/specie")