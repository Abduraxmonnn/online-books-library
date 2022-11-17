from django.urls import path, include

urlpatterns = [
    path('v1/products/', include('products.urls')),
    path('v2/categries/', include('categories.urls'))
]
