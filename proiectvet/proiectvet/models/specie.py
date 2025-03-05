from django.db import models


class Specie(models.Model):
    """Tabela specii.
    
    Tabela contine specii deja predefinite, care nu pot fi modificate sau sterse.
    Utilizatorii pot adauga specii noi pe care pot efectua CRUD.

    Pentru a putea face distinctia intre speciile predefinite si cele adaugate de utilizator,
    am adaugat un camp boolean 'protected' care este setat implicit False.
    """

    nume = models.CharField(max_length=100, unique=True)
    protected = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Specii"

    def __str__(self):
        return f"{self.id} - {self.nume}"