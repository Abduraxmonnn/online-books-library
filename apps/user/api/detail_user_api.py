# Rest-Framework
from rest_framework import views
from rest_framework.response import Response

# Project
from apps.services import get_object_by_id_or_404
from apps.user.models import User
from apps.user.serializers import UserSerializer


class UserDetailAPIView(views.APIView):
    def get(self, request, pk=None):
        queryset = get_object_by_id_or_404(User.objects, pk)
        serializer = UserSerializer(queryset, many=False)
        return Response(serializer.data)
