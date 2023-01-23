# Rest-Framework
from rest_framework import views
from rest_framework.response import Response

# Project
from apps.user.models import User
from apps.user.serializers import UserSerializer
from apps.services import list_objects


class UserListAPIView(views.APIView):

    def get(self, request):
        queryset = list_objects(User.objects)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
