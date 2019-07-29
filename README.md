# CursoDjango

O Django é um framework voltado para Web feito totalmente em Python e inspirado na produtividade do Ruby on Rails. Com Django, conseguimos fazer aplicações web rapidamente.

# Criando um projeto

 startproject, que serve para criarmos um novo projeto

$ django-admin.py startproject connectedin

O proximo passo é criar a estruturação para o Banco de Dados SQLite, que já vem instalado junto ao Django:

cd connectedin
python manage.py migrate

O manage.py é um script para gerenciar a aplicação com Django, que deve ser executado através do interpretador python dentro da pasta do projeto. 

# Colocando o projeto no ar

Agora que já temos nosso projeto criado e devidamente preparado, podemos subir nossa aplicação usando novamente o script manage.py

python manage.py runserver

# Separando responsabilidades através de aplicações

Quando criamos o projeto connectedin no Django não significa que já temos uma aplicação! Na verdade, podemos ter mais de uma aplicação por projeto. Uma aplicação no Django é uma forma de dividir a responsabilidade dentro do projeto, ou seja, é um módulo que confina dentro dele determinada responsabilidade. Criamos uma aplicação através do comando python manage.py startapp <nome da aplicaçãoca>. Dentro  da pasta raiz connectedin:

python manage.py startapp perfis


