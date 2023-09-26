from django.shortcuts import render
from apps.eixos.forms import Cadastrar_Eixo
from apps.eixos.models import Eixos
from django.contrib import messages

# Create your views here.

def cadastrar_eixo(request):
    if request.method  == 'POST':
        form = Cadastrar_Eixo(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'eixos/cadastrar.html', {'form': Cadastrar_Eixo(), 'sucesso':True})
    else:
        form = Cadastrar_Eixo()

    return render(request, 'eixos/cadastrar.html', {'form':form})

def listar_eixos(request):
    if request.method == 'GET':
        eixos = Eixos.objects.all().values()
        return render(request, 'eixos/listar.html', {'eixos':eixos})

def editar_eixos(request, id_eixo):
    pass

