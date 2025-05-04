from rest_framework.response import Response
from rest_framework import viewsets, status

from proiectvet.models.consult import Consult
from proiectvet.models.pacient import Pacient
from proiectvet.serializers.consult import ConsultSerializer


class ConsultViewSet(viewsets.ModelViewSet):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer

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
            consult = Consult.objects.get(pk=pk)
            serializer = self.get_serializer(consult, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Consult.DoesNotExist:
            return Response({"error": "Consult not found!"}, status=status.HTTP_404_NOT_FOUND)
    def destroy(self, request, pk=None):
        try:
            consult = Consult.objects.get(pk=pk)
            consult.delete()
            return Response({"message": "Consult deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
        except Consult.DoesNotExist:
            return Response({"error": "Consult not found!"}, status=status.HTTP_404_NOT_FOUND)
