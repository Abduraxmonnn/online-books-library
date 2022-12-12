# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest Framework
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.products.models import Product
from apps.products.serializers import ProductSerializer, ProductDetailSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related("author")
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "category__name", "author__name"]
    filterset_fields = ["name", "category", "year", "language", "created_date"]
    ordering_fields = ["name", "year", "-id"]
    ordering = ['-id']


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def get(self, request, pk=None):
        queryset = get_object_or_404(Product, pk=pk)
        serializer = ProductDetailSerializer(queryset, many=False)
        return Response(serializer.data)
