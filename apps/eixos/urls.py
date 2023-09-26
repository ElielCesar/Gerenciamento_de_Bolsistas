from django.urls import path
from apps.eixos import views

urlpatterns = [
    path('cadastrar_eixo/', views.cadastrar_eixo, name='cadastrar_eixo'),
    path('listar_eixos/', views.listar_eixos, name='listar_eixos')
]