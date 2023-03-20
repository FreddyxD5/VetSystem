from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.pet.models import Pet, CategoryPet
from apps.pet.api.serializers import PetSerializer, CategoryPetSerializer, PetDiagnosticSerializer


class CategoryPetViewSet(viewsets.ViewSet):
    model = CategoryPet
    serializer_class = CategoryPetSerializer

    def get_queryset(self):
        queryset = self.model.objects.filter(status=True)
        return queryset
    
    def list(self, request):
        print(self.get_queryset())
        data_serializer = self.serializer_class(self.get_queryset(), many=True).data
        return Response(data_serializer, status=status.HTTP_200_OK)

    
    def create(self, request):
        data = self.request.data
        data_serializer = self.serializer_class(data = request.data)
        if data_serializer.is_valid():
            data_serializer.save()
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
        print(data)
        try:
            queryset = self.model.objects.filter(id=self.kwargs['pk']).first()
        except:
            return Response({'error':"El id no existe"}, status = status.HTTP_400_BAD_REQUEST)
        queryset.status = False
        queryset.save()
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
        
    @action(detail=True, methods=['get'])
    def get_all_pets_diagnostics(self, request, pk=None):
        queryset = self.model.objects.filter(owner=self.kwargs['pk'], status=True)
        if queryset:
            data = PetDiagnosticSerializer(queryset, many=True)
            return Response({'data':data.data}, status=status.HTTP_200_OK)
        return Response({'error':'El usuario no tiene ninguna mascota registrada'}, status= status.HTTP_400_BAD_REQUEST)
        
        
    @action(detail=True, methods=['get'])
    def obtener_mascotas_by_owner(self, request, pk=None):        
        queryset = self.model.objects.filter(owner=self.kwargs['pk'], status=True)
        if queryset:
            serializer_data = self.serializer_class(queryset, many=True).data
            return Response({"pets":serializer_data}, status=status.HTTP_200_OK)
        return Response({'error':"User doesn't not exists"},
                status = status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        data = self.request.data
        if data is not list:
            data_serializer = self.serializer_class(data = request.data)
        else:
            data_serializer = self.serializer_class(data = request.data, many=True)
                    
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({'mensaje':'Mascota creada correctamente'}, status= status.HTTP_200_OK)
        return Response({'Error':data_serializer.errors}, status= status.HTTP_400_BAD_REQUEST)

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
        print(data)
        try:
            queryset = self.model.objects.filter(id=self.kwargs['pk']).first()
        except:
            return Response({'error':"El id no existe"}, status = status.HTTP_400_BAD_REQUEST)
        queryset.status = False
        queryset.save()
        return Response({'message':"Eliminado correctamente"}, status=status.HTTP_200_OK)

