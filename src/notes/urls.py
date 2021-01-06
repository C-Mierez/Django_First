from django.urls import path
from .views import notesOverview, noteList, noteDetail, noteCreate, noteUpdate, noteDelete

urlpatterns = [
    path('', notesOverview, name='notes-overview'),
    path('note-list/', noteList, name='note-list'),
    path('note-detail/<str:pk>/', noteDetail, name='note-detail'),
    path('note-create/', noteCreate, name='note-create'),
    path('note-update/<str:pk>', noteUpdate, name='note-update'),
    path('note-delete/<str:pk>', noteDelete, name='note-delete'),
]
