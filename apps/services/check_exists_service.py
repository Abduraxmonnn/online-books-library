# Django
from rest_framework import status
from rest_framework.response import Response


def check_exists(*args):
    for element in args:
        if element.exists():
            return Response({
                'error': f'{element} exists'
            }, status=status.HTTP_400_BAD_REQUEST)
