# Rest-Framework
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Project
from apps.user.models import User
from apps.services import filter_objects, create_user, create_token, check_exists


def signup_user(serializer, request):
    check_serializer = serializer(data=request.data, context={
        'reqeust': request
    })
    check_serializer.is_valid(raise_exception=True)
    first_name = check_serializer.validated_data['first_name']
    username = check_serializer.validated_data['username']
    password = check_serializer.validated_data['password']
    email = check_serializer.validated_data['email']
    age = check_serializer.validated_data['age']

    check_user = filter_objects(User.objects, username__iexact=username)

    check_exists(check_user)

    user = create_user(User.objects, username=username, password=password)
    user.first_name = first_name
    user.age = age
    user.email = email
    user.save()
    token = create_token(Token.objects, user=user)
    return Response({
        'token': token.key
    })
