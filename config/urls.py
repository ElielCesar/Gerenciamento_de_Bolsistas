
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.usuarios.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('usuarios/', include('apps.usuarios.urls')),
    path('sistema/', include('apps.inicio.urls')),
    path('eixos/', include('apps.eixos.urls')),
    path('bolsistas/', include('apps.bolsistas.urls')),
    path('pagamentos/', include('apps.pagamentos.urls')),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])