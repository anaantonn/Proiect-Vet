from django.db import models

from .pacient import Pacient


class Vaccin(models.Model):
    """Table for vaccinations."""
    id_pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    model_vaccin = models.CharField(max_length=100)
    data_vaccinare = models.DateField()

    def __str__(self):
        return self.model_vaccin
