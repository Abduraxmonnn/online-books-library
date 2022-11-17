from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet, ProductDetailViewSet

urlpatterns = [
    path(r'list/', ProductViewSet.as_view()),
    path(r'detail/<int:pk>/', ProductDetailViewSet.as_view()),
]
