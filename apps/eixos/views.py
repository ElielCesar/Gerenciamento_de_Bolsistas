from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from apps.eixos.forms import Cadastrar_Eixo
from apps.eixos.models import Eixos
from django.contrib import messages


# Create your views here.
@login_required 
def cadastrar_eixo(request):
    if request.method  == 'POST':
        form = Cadastrar_Eixo(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'eixos/cadastrar.html', {'form': Cadastrar_Eixo(), 'sucesso':True})
    else:
        form = Cadastrar_Eixo()

    return render(request, 'eixos/cadastrar.html', {'form':form})


@login_required
def listar_eixos(request):
    if request.method == 'GET':
        eixos = Eixos.objects.all().values()
        return render(request, 'eixos/listar.html', {'eixos':eixos})


@login_required
def editar_eixo(request):
    if request.method == 'GET':
        eixos = Eixos.objects.all().values()
        return render(request, 'eixos/editar.html', {'eixos':eixos})

@login_required
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
    eixo = get_object_or_404(Eixos, pk=id_eixo)

    if request.method == 'POST':
        eixo.delete()
        return redirect('editar_eixo')
    else:
        return render(request, 'eixos/confirmar.html', {'eixo':eixo})

