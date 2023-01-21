# Rest-Framework
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Project
from apps.user.models import User
from apps.user.serializers import UserSerializer


class UserRetrieveViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
