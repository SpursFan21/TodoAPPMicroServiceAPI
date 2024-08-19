from django.shortcuts import render
from rest_framework import generics
from todoapi.models import Todo
from todoapi.serializers import TodoAllDetailsSerializer, TodoSummarySerializer

# Create your views here.
