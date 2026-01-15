from rest_framework.response import Response
from rest_framework import viewsets, status

from proiectvet.models.client import Client
from proiectvet.models.pacient import Pacient
from proiectvet.serializers.pacient import PacientSerializer


class PacientViewSet(viewsets.ModelViewSet):
    queryset = Pacient.objects.all()
    serializer_class = PacientSerializer

    def create(self, request):
        data = request.data.copy()
        id_proprietar = data.get("id_proprietar")

        try:
            Client.objects.get(pk=id_proprietar)
        except Client.DoesNotExist:
            return Response(
                {"error": "Proprietar not found!"},
                status=status.HTTP_404_NOT_FOUND
                )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            pacient = Pacient.objects.get(pk=pk)
            serializer = self.get_serializer(
                pacient,
                data=request.data,
                partial=True
                )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
        except Pacient.DoesNotExist:
            return Response(
                {"error": "Pacient not found!"},
                status=status.HTTP_404_NOT_FOUND
                )

    def destroy(self, request, pk=None):
        try:
            pacient = Pacient.objects.get(pk=pk)
            pacient.delete()
            return Response({"message": "Pacient deleted successfully!"})
        except Pacient.DoesNotExist:
            return Response(
                {"error": "Pacient not found!"},
                status=status.HTTP_404_NOT_FOUND
                )
