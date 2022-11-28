from django.urls import path

from apps.products.views import ProductViewSet, ProductDetailViewSet

urlpatterns = [
    path(r'list/', ProductViewSet.as_view()),
    path(r'detail/<int:pk>/', ProductDetailViewSet.as_view()),
]
