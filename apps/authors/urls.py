# Django
from django.urls import path

# Project
from apps.authors.views import AuthorListAPIView, AuthorDetailAPIView

urlpatterns = [
    path(r'list', AuthorListAPIView.as_view(), name='category'),
    path(r'detail/<int:pk>', AuthorDetailAPIView.as_view(), name='author-detail')
]
