# Django REST framework
from rest_framework import viewsets

# Project
from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    search_fields = ('name', )
    ordering_fields = ('name', 'created_date')
