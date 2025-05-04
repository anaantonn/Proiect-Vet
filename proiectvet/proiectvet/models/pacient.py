from django.db import models

from .client import Client
from .rasa import Rasa


class Pacient(models.Model):
    """Pacient table."""
    id_proprietar = models.ForeignKey(Client, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100)
    sex = models.BooleanField(default=False)
    data_nasterii = models.DateField()
    microcip = models.CharField(max_length=100, unique=True, blank=True)
    sterilizat = models.BooleanField(default=False)
    id_rasa = models.ForeignKey(Rasa, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nume
