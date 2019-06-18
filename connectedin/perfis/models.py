# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Perfil(object):

    def __init__(self,name='',email='',fone='',company=''):
        self.name = name
        self.email = email
        self.fone = fone
        self.company = company

# Create your models here.
