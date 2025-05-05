from django.db import models

from .pacient import Pacient


def imagistica_path(instance, filename):
    """Function to set the path for the imagistica files."""
    pacient = instance.id_pacient
    folder_name = f"{pacient.id}_{pacient.nume.replace(" ", "_")}"
    return f"{folder_name}/imagistica/{filename}"

def analize_path(instance, filename):
    """Function to set the path for the analize files."""
    pacient = instance.id_pacient
    folder_name = f"{pacient.id}_{pacient.nume.replace(" ", "_")}"
    return f"{folder_name}/analize/{filename}"


class Consult(models.Model):
    """Consult table."""
    id_pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    anamneza = models.TextField()
    temperatura = models.FloatField()
    greutate = models.FloatField()
    heart_rate = models.IntegerField()
    observatii = models.TextField()
    tratament = models.TextField()
    imagistica = models.FileField(upload_to=imagistica_path, blank=True)
    analize = models.FileField(upload_to=analize_path, blank=True)

    def __str__(self):
        return self.data.strftime("%Y-%m-%d %H:%M:%S") + " - " + self.id_pacient.nume
