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

    def save(self, *args, **kwargs):
        """ Speciile predefinite nu pot fi modificate. """
        if self.pk and self.protected:
            raise ValueError("Nu puteti modifica speciile predefinite.")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """ Speciile predefinite nu pot fi sterse. """
        if self.protected:
            raise ValueError("Nu puteti sterge speciile predefinite.")
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nume

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

    def save(self, *args, **kwargs):
        """ Rasele predefinite nu pot fi modificate. """
        if self.pk and self.protected:
            raise ValueError("Nu puteti modifica rasele predefinite.")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """ Rasele predefinite nu pot fi sterse. """
        if self.protected:
            raise ValueError("Nu puteti sterge rasele predefinite.")
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nume