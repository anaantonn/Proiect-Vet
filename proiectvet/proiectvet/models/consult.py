from django.db import models

from .pacient import Pacient


class Consult(models.Model):
    """Consult table."""
    data = models.DateField()
    anamneza = models.TextField()
    temperatura = models.FloatField()
    greutate = models.FloatField()
    heart_rate = models.IntegerField()
    observatii = models.TextField()
    investigatii = models.FileField(upload_to="imagistica/")
    id_pacient = models.OneToOneField(Pacient, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.anamneza
