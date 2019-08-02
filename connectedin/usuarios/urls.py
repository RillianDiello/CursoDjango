from django.conf.urls import url
from django.contrib import admin
from usuarios import views
from views import RegistrarUsuarioView

urlpatterns = [  
	url(r'^registrar/$', RegistrarUsuarioView.as_view(), name="registrar")
]