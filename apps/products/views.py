# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest Framework
from rest_framework import views, viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.products.models import Product
from apps.products.serializers import ProductSerializer, ProductDetailSerializer
from apps.services import list_objects_by_select_related, get_object_by_id_or_404_and_by_prefetch_related


class ProductListViewSet(viewsets.ModelViewSet):
    queryset = list_objects_by_select_related(Product.objects, 'author')
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "category__name", "author__name"]
    filterset_fields = ["name", "category", "year", "language", "created_date"]
    ordering_fields = ["name", "year", "-id"]
    ordering = ['-id']


class ProductDetailAPIView(views.APIView):
    def get(self, request, pk=None):
        queryset = get_object_by_id_or_404_and_by_prefetch_related(Product.objects, pk, 'author', 'category')
        serializer = ProductDetailSerializer(queryset, many=False)
        return Response(serializer.data)
