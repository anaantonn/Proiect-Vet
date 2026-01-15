from rest_framework.response import Response
from rest_framework import viewsets, status

from proiectvet.models.deparazitare import Deparazitare
from proiectvet.models.pacient import Pacient
from proiectvet.serializers.deparazitare import DeparazitareSerializer


class DeparazitareViewSet(viewsets.ModelViewSet):
    queryset = Deparazitare.objects.all()
    serializer_class = DeparazitareSerializer

    def create(self, request):
        data = request.data.copy()
        id_pacient = data.get("id_pacient")

        try:
            Pacient.objects.get(pk=id_pacient)
        except Pacient.DoesNotExist:
            return Response(
                {"error": "Pacient not found!"},
                status=status.HTTP_404_NOT_FOUND
                )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            deparazitare = Deparazitare.objects.get(pk=pk)
            serializer = self.get_serializer(
                deparazitare,
                data=request.data,
                partial=True
                )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Deparazitare.DoesNotExist:
            return Response(
                {"error": "Deparazitare not found!"},
                status=status.HTTP_404_NOT_FOUND
                )

    def destroy(self, request, pk=None):
        try:
            deparazitare = Deparazitare.objects.get(pk=pk)
            deparazitare.delete()
            return Response({"message": "Deparazitare deleted successfully!"})
        except Deparazitare.DoesNotExist:
            return Response(
                {"error": "Deparazitare not found!"},
                status=status.HTTP_404_NOT_FOUND
                )
