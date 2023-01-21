# Rest-Framework
from rest_framework import serializers
# Project
from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
