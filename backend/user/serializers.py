from rest_framework import serializers
from .models import User
# from rest_framework_jwt.settings import api_settings
# from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


