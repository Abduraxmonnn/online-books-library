# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest Framework
from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.products.models import Product
from apps.products.serializers import ProductSerializer, ProductDetailSerializer


class ProductViewSet(views.APIView):
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["^name", "^category", "^author"]
    filterset_fields = ["name", "category", "year", "language", "created_date"]
    ordering_fields = ["name", "year", "-id"]
    ordering = ['-id']

    def get(self, request):
        queryset = Product.objects.select_related("author").values("id", "name", "author__name", "year",
                                                                   "language", "image", "created_date", "last_update")
        return Response(queryset)


class ProductDetailViewSet(views.APIView):
    def get(self, request, pk=None):
        queryset = get_object_or_404(Product, pk=pk)
        serializer = ProductDetailSerializer(queryset, many=False)
        return Response(serializer.data)
