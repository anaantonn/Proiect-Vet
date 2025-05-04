from django.db import models

from .pacient import Pacient


class Consult(models.Model):
    """Consult table."""
    data = models.DateTimeField(auto_now_add=True)
    anamneza = models.TextField()
    temperatura = models.FloatField()
    greutate = models.FloatField()
    heart_rate = models.IntegerField()
    observatii = models.TextField()
    investigatii = models.FileField(upload_to="imagistica/", blank=True)
    id_pacient = models.ForeignKey(Pacient, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.anamneza
