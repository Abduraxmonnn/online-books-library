# Django
from django.conf.urls import url

# Project
from categories.views import CategoryViewSet

urlpatterns = [
    url(r'category', CategoryViewSet.as_view({'get': 'list'}), name='category')
]
