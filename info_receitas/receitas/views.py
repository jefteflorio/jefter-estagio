from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Receitas
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    receitas = Receitas.objects.all()
    return render(request, 'receitas/index.html', {'receitas' : receitas})

def gravar_receita(request):
    nome_receita = request.POST['nome_receita']
    ingredientes = request.POST['ingredientes']
    inserir = Receitas(nome_receita=nome_receita,ingredientes=ingredientes )
    inserir.save()
    return HttpResponseRedirect(reverse('receitas:index'))
    
def editar_receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    return render(request, 'receitas/editar.html', {'receita': receita})

def criar_receita(request):
    return render(request, 'receitas/gravar.html')

def atualizar_receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    ingredientes = request.POST['ingredientes']
    receita.ingredientes = ingredientes
    receita.save()
    return HttpResponseRedirect(reverse('receitas:index'))

def deletar_receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    receita.delete()
    return HttpResponseRedirect(reverse('receitas:index'))

