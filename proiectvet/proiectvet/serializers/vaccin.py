from rest_framework import serializers

from proiectvet.models.vaccin import Vaccin


class VaccinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vaccin
        fields = "__all__"
