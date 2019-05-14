from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from rmp.views import (
    index,
    contact,
    about,
    databases,
    rmp,
    tri,
    nrc,
    rcris,
    brs,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.as_view(), name='index'),
    path('contact/', contact.as_view(), name='contact'),
    path('databases/', databases.as_view(), name='databases'),
    path('about/', about.as_view(), name='about'),
    path('tri/', tri.as_view(), name='tri'),
    path('nrc/', nrc.as_view(), name='nrc'),
    path('rcris/', rcris.as_view(), name='rcris'),
    path('brs/', brs.as_view(), name='brs'),
    path('rmp/', include('rmp.urls', namespace='rmp')),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
