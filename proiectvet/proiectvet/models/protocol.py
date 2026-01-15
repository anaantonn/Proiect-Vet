from django.db import models


class Protocol(models.Model):
    """Table for treatment protocols."""
    nume = models.CharField(max_length=100)
    descriere = models.TextField()

    class Meta:
        verbose_name_plural = "Protocoale"

    def __str__(self):
        return self.nume
