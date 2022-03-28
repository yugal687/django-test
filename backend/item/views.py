from urllib import request
from django.shortcuts import render, redirect
from item.serializers import ItemSerializer, CategorySerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from item.models import Item, Category


class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    # return Response(serializer_class.data)


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

# test



def index(request):
    return render(request, 'index.html', {"name": 'yugal'})


def home(request):
    return render(request, 'home.html')
