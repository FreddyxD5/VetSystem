from rest_framework import viewstes, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.diagnostic.models import Diagnostic


class DiagnosticViewSet(viewstes.GenericViewSet):
    model = Diagnostic
    #serializer_class = DiagnosticSerializer

    def get_queryset(self):
        queryset = self.model.objects.filter(status=True)        
        return queryset

    def list(self, request):
        print("something something :D")
        return Response({'data':"data"},
                    status= status.HTTP_200_OK)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass
    
    def destroy(self, request, pk=None):
        pass