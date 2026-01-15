from rest_framework import serializers

from proiectvet.models.consult import Consult


class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = "__all__"
