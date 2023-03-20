from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.diagnostic.models import Diagnostic
from apps.diagnostic.api.serializers import DiagnosticSerializer


class DiagnosticViewSet(viewsets.GenericViewSet):
    model = Diagnostic
    serializer_class = DiagnosticSerializer

    def get_queryset(self):
        queryset = self.model.objects.filter(active=True)        
        return queryset

    def list(self, request):
        print("something something :D")

        print(self.get_queryset())
        data = self.serializer_class(self.get_queryset(), many=True)

        return Response({'data':data.data},
                    status= status.HTTP_200_OK)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass
    
    def destroy(self, request, pk=None):
        pass