from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Profiles_API import serializers

# Create your views here.
class HelloApiView(APIView):
    
    serializers_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """ Retornar lista de caracteristicas del APIView """
        apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Da mayor control sobre la lofica de la aplicacion',
            'Esta mapeado manualmente a los URLs'
        ]
        
        return Response({'message' : 'Hello',
                         'apiview' : apiview})
        
    def post(self, request):
        serializer = self.serializers_class(data= request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})
        
    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})