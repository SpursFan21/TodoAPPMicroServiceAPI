from rest_framework import generics
from todoapi.models import Todo
from todoapi.serializers import TodoAllDetailsSerializer, TodoSummarySerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
#List create API view allows us to POST i.e. create a new object
# Or list all objects
class ListTodo(generics.ListCreateAPIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]	
	queryset = Todo.objects.all()
	serializer_class = TodoAllDetailsSerializer
 
# This API view allows us to do GET by id,
# UPDATE i.e. PUT by specifying the id of the todo-task
# DELETE i.e. DELETE the todo-ask we want to delete by specifying the id of the task
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]	
	queryset = Todo.objects.all()
	serializer_class = TodoAllDetailsSerializer