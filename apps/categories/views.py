# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest Framework
from rest_framework import views
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer
from apps.services import list_objects, get_object_by_id_or_404


class CategoryListAPIView(views.APIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', ]
    filterset_fields = ['name', 'created_date']
    ordering_fields = ['name', 'created_date']
    ordering = ['-id']

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        queryset = self.filter_queryset(list_objects(Category.objects))
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryDetailAPIView(views.APIView):

    def get(self, request, pk=None):
        queryset = get_object_by_id_or_404(Category, pk)
        serializer = CategorySerializer(queryset, many=False)
        return Response(serializer.data)
