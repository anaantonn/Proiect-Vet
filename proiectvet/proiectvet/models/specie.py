from django.db import models


class Specie(models.Model):
    """Species table."""

    nume = models.CharField(max_length=100, unique=True)
    protected = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Specii"

    def __str__(self):
        return self.nume
