# Rest-Framework
from rest_framework import viewsets
from rest_framework.response import Response

# Project
from apps.user.models import User
from apps.user.serializers import UserSerializer


class UserListViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
