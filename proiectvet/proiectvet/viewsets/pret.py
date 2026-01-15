from rest_framework.response import Response
from rest_framework import viewsets, status

from proiectvet.models.pret import Pret
from proiectvet.serializers.pret import PretSerializer


class PretViewSet(viewsets.ModelViewSet):
    queryset = Pret.objects.all()
    serializer_class = PretSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            pret = Pret.objects.get(pk=pk)
            serializer = self.get_serializer(
                pret,
                data=request.data, partial=True
                )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
        except Pret.DoesNotExist:
            return Response(
                {"error": "Pret not found!"},
                status=status.HTTP_404_NOT_FOUND
                )

    def destroy(self, request, pk=None):
        try:
            pret = Pret.objects.get(pk=pk)
            pret.delete()
            return Response({"message": "Pret deleted successfully!"})
        except Pret.DoesNotExist:
            return Response(
                {"error": "Pret not found!"},
                status=status.HTTP_404_NOT_FOUND
                )
