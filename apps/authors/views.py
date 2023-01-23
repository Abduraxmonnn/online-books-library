# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest Framework
from rest_framework import views
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.authors.models import Author
from apps.authors.serializers import AuthorSerializer
from apps.services import list_objects, get_object_by_id_or_404

class AuthorListAPIView(views.APIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', ]
    filterset_fields = ['name', 'created_date', 'last_update']
    ordering_fields = ['name', 'created_date']
    ordering = ['-id']

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        queryset = self.filter_queryset(list_objects(Author.objects))
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)


class AuthorDetailAPIView(views.APIView):

    def get(self, request, pk=None):
        queryset = get_object_by_id_or_404(Author, pk)
        serializer = AuthorSerializer(queryset, many=False)
        return Response(serializer.data)
