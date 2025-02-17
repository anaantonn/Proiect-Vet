from django import forms
from cabinet.models.rasa import Rasa

class AdaugaRasaForm(forms.ModelForm):
    nume = forms.CharField(label="Rasa", max_length=50)
    class Meta:
        model = Rasa
        fields = ["nume"]