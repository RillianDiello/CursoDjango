from django.shortcuts import render
from perfis.models import Perfil
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def exibir(request,perfil_id):
    perfil = Perfil()

    if perfil_id == '1':
        perfil = Perfil('Rillian Diello', 'rillian@email.com', '67999999', 'aluraCurso')  
    if perfil_id == '1':
        perfil = Perfil('Lucas Pires', 'lucas@email.com', '17955555', 'aluraCurso')  
    
    return render(request,'perfil.html',{"perfil": perfil})

