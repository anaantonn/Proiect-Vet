from django.db import models

from .pacient import Pacient


class Deparazitare(models.Model):
    """Table for flea and dweorming treatments."""
    id_pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100)
    data_administrare = models.DateField()

    class Meta:
        verbose_name_plural = "Deparazitari"

    def __str__(self):
        return self.nume
