from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from rmp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('databases/', views.databases, name='databases'),
    path('about/', views.about, name='about'),
    path('tri/', views.tri, name='tri'),
    path('nrc/', views.nrc, name='nrc'),
    path('rcris/', views.rcris, name='rcris'),
    path('brs/', views.brs, name='brs'),
    path('rmp/', include('rmp.urls', namespace='rmp')),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
