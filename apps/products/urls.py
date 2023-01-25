from django.urls import path

from apps.products.views import ProductListViewSet, ProductDetailAPIView

urlpatterns = [
    path(r'list/', ProductListViewSet.as_view({'get': 'list'})),
    path(r'detail/<int:pk>/', ProductDetailAPIView.as_view()),
]
