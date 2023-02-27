from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.pet.models import Pet, CategoryPet
from apps.pet.api.serializers import PetSerializer, CategoryPetSerializer


class CategoryPetViewSet(viewsets.ViewSet):
    model = CategoryPet
    serializer_class = CategoryPetSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset
    
    def list(self, request):
        print(self.get_queryset())
        data_serializer = self.serializer_class(self.get_queryset(), many=True).data
        return Response(data_serializer, status=status.HTTP_200_OK)

    def create(self, request):
        data = self.request.data
        data_serializer = self.serializer_class(data = request.data)
        if data_serializer.is_valid():
            return Response({'mensaje':'Categoria creada correctamente'}, status= status.HTTP_200_OK)
        return Response({'Error':'Error'}, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            queryset = self.model.objects.filter(id=pk).first()
        except:
            return Response({'Error':"El id no existe"}, status=status.HTTP_400_BAD_REQUEST)        
        queryset.status = False
        queryset.save()
        return Response({'message':"Actualizado correctamente"}, status=status.HTTP_200_OK)
        

    def destroy(self, request, pk=None):
        data = self.kwargs['pk']        
        return Response({'message':"Eliminado correctamente"}, status=status.HTTP_200_OK)


class PetViewSet(viewsets.ViewSet):
    model = Pet
    serializer_class = PetSerializer

    def get_queryset(self):
        queryset = self.model.objects.filter(status=True)        
        return queryset

    
    def list(self, request):
        data = self.serializer_class(self.get_queryset(), many=True)
        return Response(data.data, status=status.HTTP_200_OK)   
