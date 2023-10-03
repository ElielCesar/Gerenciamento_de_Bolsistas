from django.urls import path
from apps.eixos import views

urlpatterns = [
    path('', views.listar_eixos, name='listar_eixos'),
    path('cadastrar_eixo/', views.cadastrar_eixo, name='cadastrar_eixo'),
    path('listar_eixos/', views.listar_eixos, name='listar_eixos'),
    path('editar_eixo/', views.editar_eixo, name='editar_eixo'),
    path('detalhes/<int:id_eixo>/', views.detalhes_eixo, name='detalhes_eixo'),
    path('deletar_eixo/<int:id_eixo>/', views.deletar_eixo, name='deletar_eixo')
]