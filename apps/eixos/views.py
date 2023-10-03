from django.contrib.auth.decorators import login_required, user_passes_test
from apps.permissions import is_bolsista, is_coordenador
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from apps.eixos.forms import Cadastrar_Eixo
from apps.eixos.models import Eixos

# Create your views here.

@login_required 
@user_passes_test(is_coordenador)
def cadastrar_eixo(request):
    # verifica se o usuario está no grupo, retorna True ou False
    grupo_usuario = request.user.groups.filter(name='Coordenadores').exists()

    if request.method  == 'POST':
        form = Cadastrar_Eixo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eixos')
    else:
        form = Cadastrar_Eixo()

    return render(request, 'eixos/cadastrar.html', {'form':form, 'grupo_usuario': grupo_usuario})


@login_required
@user_passes_test(is_coordenador)
def editar_eixo(request):
    # verifica se o usuario esta no grupo citado, retorna True ou False
    grupo_usuario = request.user.groups.filter(name='Coordenadores').exists()

    if request.method == 'GET':
        eixos = Eixos.objects.all().values()
        return render(request, 'eixos/editar.html', {'eixos':eixos, 'grupo_usuario':grupo_usuario})


@login_required
@user_passes_test(is_coordenador)
def detalhes_eixo(request, id_eixo):
    eixo = get_object_or_404(Eixos, pk=id_eixo)
    
    if request.method == 'POST':
        form = Cadastrar_Eixo(request.POST, instance=eixo)
        if form.is_valid():
            form.save()
            return redirect('editar_eixo')
    else:
        form = Cadastrar_Eixo(instance=eixo)

    return render(request, 'eixos/update.html', {'form': form, 'eixo':eixo})


@login_required
def deletar_eixo(request, id_eixo):
    # verifica se o usuario está no grupo
    grupo_usuario = request.user.groups.filter(name='Coordenadores').exists()
    eixo = get_object_or_404(Eixos, pk=id_eixo)

    if request.method == 'POST':
        eixo.delete()
        return redirect('editar_eixo')
    else:
        return render(request, 'eixos/confirmar.html', {'eixo':eixo})


@login_required
def listar_eixos(request):
    if request.method == 'GET':
        eixos = Eixos.objects.all().values()
        return render(request, 'eixos/listar.html', {'eixos':eixos})