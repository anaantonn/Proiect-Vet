from rest_framework import serializers

from proiectvet.models.deparazitare import Deparazitare


class DeparazitareSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deparazitare
        fields = "__all__"
