# Rest-Framework
from rest_framework import serializers

# Project
from apps.user.models import User


class UserSignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'password',
            'email',
            'age'
        ]
