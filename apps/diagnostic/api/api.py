from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.diagnostic.models import Diagnostic
from apps.diagnostic.api.serializers import DiagnosticSerializer
import json


class DiagnosticViewSet(viewsets.GenericViewSet):
    model = Diagnostic
    serializer_class = DiagnosticSerializer

    def get_queryset(self):
        queryset = self.model.objects.filter(active=True)        
        return queryset

    def list(self, request):
        data = self.serializer_class(self.get_queryset(), many=True)
        return Response({'data':data.data},
                    status= status.HTTP_200_OK)

    def create(self, request):        
        data = request.data['diagnostic']
        # data_diagnostic = json.loads(request.data['diagnostic'])
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'diagnostico creado'}, status=status.HTTP_201_CREATED)        
        return Response({'error':serializers.error}, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        try:
            queryset = self.model.objects.get(id = self.kwargs['pk'])
        except:
            return Response({'error':'diagnostic doesnot exists'}, status=status.HTTP_400_BAD_REQUEST)        
        data_update = request.data['diagnostic']
        print(data_update)
        # data_update = json.loads(request.data['diagnostic'])
        diagnostic_serializer = self.serializer_class(queryset, data=data_update)
        if diagnostic_serializer.is_valid():
            diagnostic_serializer.save()
            return Response({'message':'Diagnostic update!'}, status=status.HTTP_200_OK)
        return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        try:
            queryset = self.model.objects.get(id = self.kwargs['pk'])
        except:
            return Response({'error':'diagnostic doesnot exists'}, status=status.HTTP_400_BAD_REQUEST) 
        queryset.status=False
        queryset.save()
        return Response({'message':'Diagnostic Deleted'}, status=status.HTTP_200_OK)
    