from django.urls import path, include

urlpatterns = [
    path('v1/user/', include('apps.user.urls')),
    path('v2/products/', include('apps.products.urls')),
    path('v3/categries/', include('apps.categories.urls')),
    path('v4/authors/', include('apps.authors.urls')),
]
