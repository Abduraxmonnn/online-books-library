from django.urls import path

from apps.products.views import ProductAPIView, ProductDetailAPIView

urlpatterns = [
    path(r'list/', ProductAPIView.as_view()),
    path(r'detail/<int:pk>/', ProductDetailAPIView.as_view()),
]
