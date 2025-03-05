from rest_framework.response import Response
from rest_framework import viewsets, status
from proiectvet.models.specie import Specie
from proiectvet.serializers.specie import SpecieSerializer


class SpecieViewSet(viewsets.ModelViewSet):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        try:
            specie = Specie.objects.get(pk=pk)
            if specie.protected:    
                return Response({"error": "Specie cannot be modified!"}, status=status.HTTP_400_BAD_REQUEST)
        
            serializer = self.get_serializer(specie, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Specie.DoesNotExist:
            return Response({"error": "Specie not found!"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
            try:
                specie = Specie.objects.get(pk=pk)
                if specie.protected:    
                    return Response({"error": "Specie cannot be modified!"}, status=status.HTTP_400_BAD_REQUEST)
                specie.delete()
                return Response({"message": "Specie deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
        
            except Specie.DoesNotExist:
                return Response({"error": "Specie not found!"}, status=status.HTTP_404_NOT_FOUND)