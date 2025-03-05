from rest_framework import serializers
from proiectvet.models.rasa import Rasa


class RasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasa
        fields = "__all__"