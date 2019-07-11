from django.conf.urls import url
from django.contrib import admin
from perfis import views

urlpatterns = [    
    url(r'^$', views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar')
]