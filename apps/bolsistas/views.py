from django.shortcuts import render, redirect, get_object_or_404
from apps.bolsistas.forms import Cadastrar_Bolsista
from apps.bolsistas.models import Bolsista 

# SISTEMA DE CRUD - INICIO
def cadastrar_bolsistas(request):
     if request.method == 'POST':
          form = Cadastrar_Bolsista(request.POST)
          if form.is_valid():
               form.save()
               form = Cadastrar_Bolsista()
               return redirect('listar_bolsistas')
          
     else:
          form = Cadastrar_Bolsista()
     
     return render(request, 'bolsistas/cadastrar.html', {'form':form})


def editar_bolsistas(request):
     if request.method == 'GET':
          bolsistas = Bolsista.objects.all().values()
          return render(request, 'bolsistas/editar.html', {'bolsistas':bolsistas})


def listar_bolsistas(request):
     if request.method == 'GET':
          bolsistas = Bolsista.objects.all().values()
          return render(request, 'bolsistas/listar.html', {'bolsistas':bolsistas})


def deletar_bolsistas(request, id_bolsista):
     bolsista = get_object_or_404(Bolsista, pk=id_bolsista)

     if request.method == 'POST':
          bolsista.delete()
          return redirect('editar_bolsistas')

     else:
          return render(request, 'bolsistas/confirmar.html', {'bolsista':bolsista})


def detalhes_bolsista(request, id_bolsista):
     bolsista = get_object_or_404(Bolsista, pk=id_bolsista)

     if request.method == 'POST':
          form = Cadastrar_Bolsista(request.POST, instance=bolsista)
          if form.is_valid():
               form.save()
               return redirect('editar_bolsistas')

     else:
          form = Cadastrar_Bolsista(instance=bolsista)

     return render(request, 'bolsistas/update.html', {'form':form, 'bolsista':bolsista})
# SISTEMA DE CRUD - FIM 