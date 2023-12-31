from django.contrib.auth.decorators import login_required, user_passes_test
from apps.permissions import is_bolsista, is_coordenador, is_financeiro
from django.shortcuts import render, redirect, get_object_or_404
from apps.pagamentos.models import Relatorio
from apps.pagamentos.forms import Cadastrar_Relatorio

# Sistema de CRUD parcial - inicio 
@login_required
def cadastrar_relatorio(request):
    if request.method == 'POST':
        form = Cadastrar_Relatorio(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_solicitacoes')

    else:
        form = Cadastrar_Relatorio()
    
    return render(request, 'pagamentos/cadastrar.html', {'form': form})


@login_required
def listar_solicitacoes(request):
    if request.method == 'GET':
        solicitacoes = Relatorio.objects.all().select_related('bolsista')
        print(solicitacoes)
        return render(request, 'pagamentos/listar.html', {'solicitacoes':solicitacoes})

# Sistema de CRUD parcial - fim

# view que autoriza os pagamentos
@login_required
@user_passes_test(is_financeiro)
def autorizar_pagamentos(request):
    
    if request.method == 'GET':
        solicitacoes = Relatorio.objects.all().select_related('bolsista')
        return render(request, 'pagamentos/autorizar.html', {'solicitacoes':solicitacoes})

@login_required
@user_passes_test(is_financeiro)
def detalhes_relatorio_pagamentos(request, id_solicitacao):

    form = get_object_or_404(Relatorio, pk=id_solicitacao)

    if request.method == 'POST':
        form = Cadastrar_Relatorio(request.POST, request.FILES, instance=form)
        if form.is_valid():
            form.save()
            return redirect('autorizar_pagamentos')

    else:
        form = Cadastrar_Relatorio(instance=form)

    return render(request, 'pagamentos/update.html', {'form':form})
