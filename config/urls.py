
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sistema/', include('apps.inicio.urls')),
    path('auth/login/', include('apps.usuarios.urls')),
    path('eixos/', include('apps.eixos.urls')),
    path('bolsistas/', include('apps.bolsistas.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)