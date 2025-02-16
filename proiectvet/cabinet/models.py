from django.db import models

# Create your models here.

class Client(models.Model):
    """Tabela client.
    
    Tabela contine campurile necesare adaugarii unui proprietar.
    """
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nume

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
    
class Pacient(models.Model):
    """Tabela pacient.
    
    Tabela contine campurile necesare adaugarii unui pacient.
    """

    nume = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)
    data_nastere = models.DateField()
    id_rasa = models.ForeignKey(Rasa, on_delete=models.DO_NOTHING)
    id_proprietar = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.nume

class Consult(models.Model):
    """Tabela consult.
    
    Tabela contine campurile necesare efectuarii unui consult complet.
    """

    data = models.DateField(auto_now=True)
    anamneza = models.TextField()
    temperatura = models.FloatField()
    greutate = models.FloatField()
    heart_rate = models.FloatField()
    respiratory_rate = models.FloatField()
    observatii = models.TextField()
    id_pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)

    def __str__(self):
        return self.anamneza