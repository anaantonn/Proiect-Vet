from rest_framework import serializers

from proiectvet.models.protocol import Protocol


class ProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protocol
        fields = "__all__"
