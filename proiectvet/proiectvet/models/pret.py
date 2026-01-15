from django.db import models


class Pret(models.Model):
    """Table for prices of available services."""
    nume_serviciu = models.CharField(max_length=100)
    pret = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Preturi Servicii"

    def __str__(self):
        return f"{self.nume_serviciu} - {self.pret} RON"
