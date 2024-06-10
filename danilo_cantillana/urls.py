from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', principal, name="principal"),
    path('', include('m_usuario.urls')),
    path('', include('m_producto.urls')),
    path('', include('m_venta.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)