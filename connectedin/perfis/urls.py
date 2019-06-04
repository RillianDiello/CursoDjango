from django.conf.urls import url
from django.contrib import admin
import perfis.views


urlpatterns = [    
    url(r'^$', perfis.views.index)
]