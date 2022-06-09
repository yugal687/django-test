from rest_framework import serializers
from .models import Cart
from item.serializers import ItemSerializer
# from rest_framework_jwt.settings import api_settings
# from django.contrib.auth.models import User

class CartSerializer(serializers.ModelSerializer):
    items = ItemSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ('__all__')


