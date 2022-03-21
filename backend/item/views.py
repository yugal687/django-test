from urllib import request
from django.shortcuts import render, redirect
from item.serializers import ItemSerializer 
from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.views import APIView     
from item.models import Item     

# from rest_framework.generics import ListAPIView
# from rest_framework.generics import CreateAPIView
# from rest_framework.generics import DestroyAPIView
# from rest_framework.generics import UpdateAPIView


# test

# from django.shortcuts import render, redirect
# #users
# from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User
# from rest_framework import permissions, status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import UserSerializer, UserSerializerWithToken


class ItemView(viewsets.ModelViewSet):  
    serializer_class = ItemSerializer 
    queryset = Item.objects.all()

    # return Response(serializer_class.data)


# test

def index(request):
    return render(request, 'index.html', { "name": 'yugal'})

def home(request):
    return render(request, 'home.html')

# class ListItemAPIView(ListAPIView):
#     """This endpoint list all of the available todos from the database"""
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

# class CreateItemAPIView(CreateAPIView):
#     """This endpoint allows for creation of a todo"""
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

# class UpdateItemAPIView(UpdateAPIView):
#     """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

# class DeleteItemAPIView(DestroyAPIView):
#     """This endpoint allows for deletion of a specific Todo from the database"""
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer




# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.response import Response
# from rest_framework import status

# class ItemView(viewsets.ModelViewSet):
#     parser_classes = (MultiPartParser, FormParser)
#     queryset = Item.objects.all() 
#     serializer_class = ItemSerializer

#     def get(self, request, *args, **kwargs):
#         items = Item.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         items_serializer = ItemSerializer(data=request.data)
#         if items_serializer.is_valid():
#             items_serializer.save()
#             return Response(items_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print('error', items_serializer.errors)
#             return Response(items_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





#users
# @api_view(['GET'])
# def current_user(request):
#     """
#     Determine the current user by their token, and return their data
#     """
    
#     serializer = UserSerializer(request.user)
#     return Response(serializer.data)


# class UserList(APIView):
#     """
#     Create a new user. It's called 'UserList' because normally we'd have a get
#     method here too, for retrieving a list of all User objects.
#     """

#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = UserSerializerWithToken(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)