from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action



# Create your views here.
class LoginViewSet(ViewSet):       
    def create(self, request):
        print("Creando algo")
        return Response({'token':'siu'}, status=status.HTTP_200_OK)