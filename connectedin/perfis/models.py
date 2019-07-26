# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Perfil(models.Model):

    name = models.CharField(max_length = 255, null = False)
    email = models.CharField(max_length = 255, null = False)
    fone = models.CharField(max_length = 15, null = False)
    company = models.CharField(max_length = 255, null = False)
    # Um relacionamento de muitos para muitos com relacionamento com ele mesmo por isso o self
    contatos = models.ManyToManyField('self')

    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self, convidado = perfil_convidado)
        convite.save()

    # def __init__(self,name='',email='',fone='',company=''):
    #     self.name = name
    #     self.email = email
    #     self.fone = fone
    #     self.company = company

# Create your models here.


# Aki temos uma classe que possui o um relacionamento com a classe Perfil 
# Essa relacao é dada pela presenca da ForeignKey da class Perfil
# Essa relacao é n x n
# Alem disso é passado o atributo related_name, que sera criado automaticamente  
# na classe Perfil com os nomes indicados
class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name = 'convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name = 'convites_recebidos')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante) # está adicionando na lista do perfil convidado
        self.solicitante.contatos.add(self.convidado)
        self.delete()