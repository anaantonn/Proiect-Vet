from django.contrib import admin
from proiectvet.models.client import Client
from proiectvet.models.consult import Consult
from proiectvet.models.deparazitare import Deparazitare
from proiectvet.models.pacient import Pacient
from proiectvet.models.rasa import Rasa
from proiectvet.models.specie import Specie
from proiectvet.models.vaccin import Vaccin

admin.site.register(Client)
admin.site.register(Consult)
admin.site.register(Deparazitare)
admin.site.register(Pacient)
admin.site.register(Rasa)
admin.site.register(Specie)
admin.site.register(Vaccin)
