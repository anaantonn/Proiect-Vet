from rest_framework.response import Response
from rest_framework import viewsets, status

from proiectvet.models.vaccin import Vaccin
from proiectvet.models.pacient import Pacient
from proiectvet.serializers.vaccin import VaccinSerializer


class VaccinViewSet(viewsets.ModelViewSet):
    queryset = Vaccin.objects.all()
    serializer_class = VaccinSerializer

    def create(self, request):
        data = request.data.copy()
        id_pacient = data.get("id_pacient")

        try:
            Pacient.objects.get(pk=id_pacient)
        except Pacient.DoesNotExist:
            return Response({"error": "Pacient not found!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            vaccin = Vaccin.objects.get(pk=pk)
            serializer = self.get_serializer(vaccin, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Vaccin.DoesNotExist:
            return Response({"error": "Vaccin not found!"}, status=status.HTTP_404_NOT_FOUND)
    def destroy(self, request, pk=None):
        try:
            vaccin = Vaccin.objects.get(pk=pk)
            vaccin.delete()
            return Response({"message": "Vaccin deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
        except Vaccin.DoesNotExist:
            return Response({"error": "Vaccin not found!"}, status=status.HTTP_404_NOT_FOUND)
