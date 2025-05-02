from django.db import models

from .specie import Specie


class Rasa(models.Model):
    """Breeds table."""
    nume = models.CharField(max_length=100, unique=True)
    id_specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    protected = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Rase"

    def __str__(self):
        return self.nume
