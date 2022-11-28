from django.urls import path, include

urlpatterns = [
    path('v1/products/', include('apps.products.urls')),
    path('v2/categries/', include('apps.categories.urls'))
]
