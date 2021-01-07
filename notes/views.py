from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def notesOverview(request):
    api_urls = {
        'List'      : '/note-list/',
        'Detail'    : '/note-detail/<str:pk>/',
        'Create'    : '/note-create/',
        'Update'    : '/note-update/<str:pk>/',
        'Delete'    : '/note-delete/<str:pk>/', 
    }
    return Response(api_urls)

@api_view(['GET'])
def noteList(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def noteDetail(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def noteCreate(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def noteUpdate(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(data=request.data, instance=note)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def noteDelete(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    
    return Response('Note has been deleted!', status=status.HTTP_200_OK)
