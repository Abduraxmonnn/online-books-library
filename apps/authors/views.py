from rest_framework import viewsets

from apps.authors.models import Author
from apps.authors.serializers import AuthorSerializer


class AuthorVIewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
