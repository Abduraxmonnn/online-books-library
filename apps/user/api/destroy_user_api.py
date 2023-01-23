# Django
from django.db.models import ProtectedError

# Rest-Framework
from rest_framework import status, permissions
from rest_framework import viewsets
from rest_framework.response import Response

# Project
from apps.user.models import User
from apps.user.serializers import UserSerializer


class UserDestroyViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    search_fields = ('username', 'age')
    ordering_fields = ('username', 'id')

    def get_permissions(self):
        if self.action in ['list']:
            return [permissions.AllowAny()]
        return super(UserDestroyViewSet, self).get_permissions()

    def destroy(self, request, *args, **kwargs):
        try:
            return super(UserDestroyViewSet, self).destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(data={'This object can not be deleted'}, status=status.HTTP_400_BAD_REQUEST)
