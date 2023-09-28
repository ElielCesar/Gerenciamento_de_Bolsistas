from django.urls import path
from apps.pagamentos import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_relatorio, name='cadastrar_relatorio'),
    path('listar/', views.listar_solicitacoes, name='listar_solicitacoes'),
    path('autorizar/', views.autorizar_pagamentos, name='autorizar_pagamentos'),
    path('detalhes_relatorio/<int:id_solicitacao>/', views.detalhes_relatorio_pagamentos, name='detalhes_relatorio_pagamentos'),
]