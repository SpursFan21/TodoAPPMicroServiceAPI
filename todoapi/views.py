from django.shortcuts import render
from rest_framework import generics
from todoapi.models import Todo
from todoapi.serializers import TodoAllDetailsSerializer, TodoSummarySerializer

# Create your views here.

class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()  # Use Todo directly
    serializer_class = TodoAllDetailsSerializer  # Use the appropriate serializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()  # Use Todo directly
    serializer_class = TodoAllDetailsSerializer  # Use the appropriate serializer
