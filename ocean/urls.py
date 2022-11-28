from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static


urlpatterns = (
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path(r'main/', include('apps.urls'),  name='main')
)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += path('__debug__/', include('debug_toolbar.urls'))

urlpatterns += tuple(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns += tuple(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
