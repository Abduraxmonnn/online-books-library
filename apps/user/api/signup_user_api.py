# Rest-Framework
from rest_framework import views, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Project
from apps.user.models import User
from apps.user.serializers import UserSignUpSerializer

class UserSignUpViewSet(views.APIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data, context={
            'request': request
        })
        serializer.is_valid(raise_exception=True)
        first_name = serializer.validated_data['first_name']
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        email = serializer.validated_data['email']
        age = serializer.validated_data['age']
        check_user = User.objects.filter(username__iexact=username, email__iexact=email)

        if check_user.exists():
            return Response({
                'error': 'User exists'
            }, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.age = age
        user.email = email
        user.save()
        token = Token.objects.create(user=user)
        return Response({
            'token': token.key
        })
