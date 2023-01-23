from django.urls import path

from apps.products.views import ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path(r'list/', ProductListAPIView.as_view()),
    path(r'detail/<int:pk>/', ProductDetailAPIView.as_view()),
]
