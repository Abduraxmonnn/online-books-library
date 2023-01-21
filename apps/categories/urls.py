# Django
from django.urls import path

# Project
from apps.categories.views import CategoryListAPIView, CategoryDetailAPIView

urlpatterns = [
    path(r'list', CategoryListAPIView.as_view(), name='category'),
    path(r'detail/<int:pk>', CategoryDetailAPIView.as_view(), name='category-detail')
]
