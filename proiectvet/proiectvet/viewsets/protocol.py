from rest_framework.response import Response
from rest_framework import viewsets, status

from proiectvet.models.protocol import Protocol
from proiectvet.serializers.protocol import ProtocolSerializer


class ProtocolViewSet(viewsets.ModelViewSet):
    queryset = Protocol.objects.all()
    serializer_class = ProtocolSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            protocol = Protocol.objects.get(pk=pk)
            serializer = self.get_serializer(
                protocol,
                data=request.data, partial=True
                )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
        except Protocol.DoesNotExist:
            return Response(
                {"error": "Protocol not found!"},
                status=status.HTTP_404_NOT_FOUND
                )

    def destroy(self, request, pk=None):
        try:
            protocol = Protocol.objects.get(pk=pk)
            protocol.delete()
            return Response({"message": "Protocol deleted successfully!"})
        except Protocol.DoesNotExist:
            return Response(
                {"error": "Protocol not found!"},
                status=status.HTTP_404_NOT_FOUND
                )
