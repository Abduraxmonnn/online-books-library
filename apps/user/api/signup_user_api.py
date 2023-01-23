# Rest-Framework
from rest_framework import views

# Project
from apps.user.serializers import UserSignUpSerializer
from apps.user.services.signup_serivce import signup_user


class UserSignUpViewSet(views.APIView):

    def post(self, request):
        return signup_user(UserSignUpSerializer, request)
