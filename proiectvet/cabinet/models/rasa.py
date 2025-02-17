from django.db import models
from cabinet.models.specie import Specie

# Create your models here.

class Rasa(models.Model):
    """Tabela rase.
    
    Tabela contine rase deja predefinite, care nu pot fi modificate sau sterse.
    Utilizatorii pot adauga specii noi pe care pot efectua CRUD.

    Pentru a putea face distinctia intre rasele predefinite si cele adaugate de utilizator,
    am adaugat un camp boolean 'protected' care este setat implicit False.
    """
    
    nume = models.CharField(max_length=100, unique=True)
    id_specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    protected = models.BooleanField(default=False)

    def __str__(self):
        return self.nume