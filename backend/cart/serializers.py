from rest_framework import serializers
from .models import Cart
# from rest_framework_jwt.settings import api_settings
# from django.contrib.auth.models import User

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('__all__')


