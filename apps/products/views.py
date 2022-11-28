# Rest Framework
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, views
from rest_framework.response import Response

# Project
from apps.products.models import Product
from apps.products.serializers import ProductSerializer, ProductDetailSerializer


class ProductViewSet(views.APIView):
    search_fields = ["^name", "^category", "^author"]
    filterset_fields = ["name", "category", "year", "language", "created_date"]
    ordering_fields = ["name", "year", "-id"]
    ordering = ['-id']

    def get(self, request):
        queryset = Product.objects.select_related("author").all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductDetailViewSet(views.APIView):
    def get(self, request, pk=None):
        queryset = get_object_or_404(Product, pk=pk)
        serializer = ProductDetailSerializer(queryset, many=False)
        return Response(serializer.data)
