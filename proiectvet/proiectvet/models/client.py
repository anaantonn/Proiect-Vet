from django.db import models


class Client(models.Model):
    """Client/Owner table."""
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Clienti"

    def __str__(self):
        return f"{self.nume} {self.prenume}"
