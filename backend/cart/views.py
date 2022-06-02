from django.shortcuts import render, redirect
from cart.serializers import CartSerializer
from rest_framework import viewsets
from cart.models import Cart


class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()