# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest Framework
from rest_framework import views
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.products.models import Product
from apps.products.serializers import ProductSerializer, ProductDetailSerializer
from apps.services.basic_services import get_object_by_id_or_404, list_objects_by_select_related


class ProductAPIView(views.APIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "category__name", "author__name"]
    filterset_fields = ["name", "category", "year", "language", "created_date"]
    ordering_fields = ["name", "year", "-id"]
    ordering = ['-id']

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        queryset = self.filter_queryset(list_objects_by_select_related(Product.objects, "author"))
        serializer = ProductSerializer(queryset, many=True).data
        return Response(serializer)


class ProductDetailAPIView(views.APIView):
    def get(self, request, pk=None):
        queryset = get_object_by_id_or_404(Product, pk)
        serializer = ProductDetailSerializer(queryset, many=False)
        return Response(serializer.data)
