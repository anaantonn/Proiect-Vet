from django.db import models

from .client import Client
from .rasa import Rasa


class Pacient(models.Model):
    """Pacient table"""
    id_proprietar = models.OneToOneField(Client, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100)
    sex = models.BooleanField(default=False)
    data_nasterii = models.DateField()
    id_rasa = models.ForeignKey(Rasa, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nume
