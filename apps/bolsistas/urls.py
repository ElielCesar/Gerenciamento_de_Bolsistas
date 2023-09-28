from django.urls import path
from apps.bolsistas import views

urlpatterns = [
    path('editar/', views.editar_bolsistas, name='editar_bolsistas'),
    path('cadastrar/', views.cadastrar_bolsistas, name='cadastrar_bolsistas'),
    path('listar/', views.listar_bolsistas, name='listar_bolsistas'),
    path('deletar/<int:id_bolsista>/', views.deletar_bolsistas, name='deletar_bolsistas'),
    path('detalhes/<int:id_bolsista>/', views.detalhes_bolsista, name='detalhes_bolsista')
]