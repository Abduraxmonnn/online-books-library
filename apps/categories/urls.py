# Django
from django.conf.urls import url

# Project
from apps.categories.views import CategoryViewSet

urlpatterns = [
    url(r'category', CategoryViewSet.as_view({'get': 'list'}), name='category')
]
