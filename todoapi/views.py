from rest_framework import generics
from todoapi.models import Todo
from todoapi.serializers import TodoAllDetailsSerializer, TodoSummarySerializer

class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSummarySerializer  # Or TodoAllDetailsSerializer if you need more fields

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoAllDetailsSerializer
