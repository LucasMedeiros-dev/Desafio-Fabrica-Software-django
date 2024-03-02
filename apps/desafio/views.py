from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

# View Para Criação de Conta.


class CriarContaView(CreateView):
    template_name = 'desafio/criar_conta.html'
    success_url = reverse_lazy('desafio:login')
    # Define o modelo que será utilizado
    model = User
    # Define os campos que serão utilizados
    fields = ['username', 'password']
