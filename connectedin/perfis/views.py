# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil, Convite
from django.shortcuts import redirect
# from django.http import HttpResponse

# Create your views here.

def index(request):

    return render(request,'index.html', {'perfis': Perfil.objects.all(), 'perfil_logado': get_perfil_logado(request)})

def exibir(request,perfil_id):

    perfil = Perfil.objects.get(id=perfil_id)   
    perfil_logado =  get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all() # pergunta o perfil exibido ja contato do logado
         
    return render(request,'perfil.html',{"perfil": perfil, 'ja_eh_contato': ja_eh_contato})

def convidar(request, perfil_id):
    # pass
#  pass: indicando para o Python que aquela funcao nada faz
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')

def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')

# Temos que passar o request como parametro, pois caso contrario o Django rejeitaria
# Ele espera que todas as funcoes do connectedin/perfis/view tenham o parametro, mesmo sem utiliza-lo
def get_perfil_logado(request):
    return Perfil.objects.get(id=1)


