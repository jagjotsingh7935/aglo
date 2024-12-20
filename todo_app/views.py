from django.shortcuts import render
from rest_framework import viewsets
from .models import ToDoItem
from .serializers import ToDoItemSerializer

class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

def index(request):
    return render(request, 'index.html')