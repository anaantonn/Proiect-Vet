from rest_framework import serializers
from proiectvet.models.specie import Specie


class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = "__all__"