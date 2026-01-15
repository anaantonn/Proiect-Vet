from rest_framework import serializers

from proiectvet.models.pret import Pret


class PretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pret
        fields = "__all__"
