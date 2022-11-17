from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static


urlpatterns = (
    url('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    url(r'main/', include(('apps.urls', 'main'),  namespace='main'))
)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += path('__debug__/', include('debug_toolbar.urls'))

urlpatterns += tuple(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns += tuple(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
