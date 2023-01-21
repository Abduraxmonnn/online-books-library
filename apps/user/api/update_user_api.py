# Rest-Framework
from rest_framework import status, permissions
from rest_framework import viewsets
from rest_framework.response import Response

# Project
from apps.user.models import User
from apps.user.serializers import UserSerializer


class UserUpdateViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

    search_fields = ('username', 'age')
    ordering_fields = ('username', 'id')

    def get_permissions(self):
        if self.action in ['list']:
            return [permissions.AllowAny()]
        return super(UserUpdateViewSet, self).get_permissions()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
