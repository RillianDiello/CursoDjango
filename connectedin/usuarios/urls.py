from django.conf.urls import url
from django.contrib import admin
from usuarios import views
from views import RegistrarUsuarioView



urlpatterns = [  
	url(r'^registrar/$', RegistrarUsuarioView.as_view(), name="registrar"),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url':'/login/'}, name='logout')
]