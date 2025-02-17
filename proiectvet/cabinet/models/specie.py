from django.db import models

# Create your models here.

class Specie(models.Model):
    """Tabela specii.
    
    Tabela contine specii deja predefinite, care nu pot fi modificate sau sterse.
    Utilizatorii pot adauga specii noi pe care pot efectua CRUD.

    Pentru a putea face distinctia intre speciile predefinite si cele adaugate de utilizator,
    am adaugat un camp boolean 'protected' care este setat implicit False.
    """

    nume = models.CharField(max_length=100, unique=True)
    protected = models.BooleanField(default=False)

    def __str__(self):
        return self.nume