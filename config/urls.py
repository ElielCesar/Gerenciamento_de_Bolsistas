
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
