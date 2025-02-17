from django import forms
from cabinet.models.specie import Specie

class AdaugaSpecieForm(forms.ModelForm):
    nume = forms.CharField(label="Specie", max_length=50)
    class Meta:
        model = Specie
        fields = ["nume"]