from django.shortcuts import render
from todo.serializers import TodoSerializer 
from rest_framework import viewsets, response      
from .models import Todo                 

class TodoView(viewsets.ModelViewSet):  
    serializer_class = TodoSerializer   
    queryset = Todo.objects.all() 


 