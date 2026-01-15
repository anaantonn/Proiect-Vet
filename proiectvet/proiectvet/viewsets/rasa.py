from rest_framework.response import Response
from rest_framework import viewsets, status

from proiectvet.models.rasa import Rasa
from proiectvet.models.specie import Specie
from proiectvet.serializers.rasa import RasaSerializer


class RasaViewSet(viewsets.ModelViewSet):
    queryset = Rasa.objects.all()
    serializer_class = RasaSerializer

    def create(self, request):
        data = request.data.copy()
        id_specie = data.get("id_specie")

        try:
            Specie.objects.get(pk=id_specie)
        except Specie.DoesNotExist:
            return Response(
                {"error": "Specie not found!"},
                status=status.HTTP_404_NOT_FOUND
                )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            rasa = Rasa.objects.get(pk=pk)
            if rasa.protected:
                return Response(
                    {"error": "Rasa cannot be modified!"},
                    status=status.HTTP_400_BAD_REQUEST
                    )

            serializer = self.get_serializer(
                rasa,
                data=request.data,
                partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
        except Rasa.DoesNotExist:
            return Response(
                {"error": "Rasa not found!"},
                status=status.HTTP_404_NOT_FOUND
                )

    def destroy(self, request, pk=None):
        try:
            rasa = Rasa.objects.get(pk=pk)
            if rasa.protected:
                return Response(
                    {"error": "Rasa cannot be modified!"},
                    status=status.HTTP_400_BAD_REQUEST
                    )
            rasa.delete()
            return Response({"message": "Rasa deleted successfully!"})
        except Rasa.DoesNotExist:
            return Response(
                {"error": "Rasa not found!"},
                status=status.HTTP_404_NOT_FOUND
                )
