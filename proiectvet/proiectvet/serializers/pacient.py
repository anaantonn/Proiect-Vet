from rest_framework import serializers

from proiectvet.models.pacient import Pacient


class PacientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacient
        fields = "__all__"
