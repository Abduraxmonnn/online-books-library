# Django
from django.urls import path, include

# Rest-Framework
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Project
from apps.user.api import UserSignUpViewSet, UserLogInAPIView, \
    UserUpdateViewSet, UserDestroyViewSet, UserListViewSet, UserRetrieveViewSet


router = DefaultRouter()
router.register(r'destroy',  UserDestroyViewSet, basename='destroy')
router.register(r'update',  UserUpdateViewSet, basename='update')

router.register(r'list',  UserListViewSet, basename='list')
router.register(r'retrieve',  UserRetrieveViewSet, basename='retrieve')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'signup/', UserSignUpViewSet.as_view(), name='signup'),
    path(r'login/', UserLogInAPIView.as_view(), name='login'),
    path(r'get/token/', obtain_auth_token),
]
