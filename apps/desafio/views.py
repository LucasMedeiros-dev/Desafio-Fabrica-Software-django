from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import TreinadorForm, PokemonForm
from .models import Treinador, Pokemon


class TreinadorCreateView(CreateView):
    model = Treinador
    template_name = "desafio/treinador_form.html"
    form_class = TreinadorForm
    # success_url = reverse_lazy("desafio:ver_treinador")

    def get_success_url(self) -> str:
        return reverse_lazy(f"desafio:ver_treinador", kwargs={"pk": self.object.pk})


class TreinadorUpdateView(UpdateView):
    model = Treinador
    template_name = "desafio/treinador_form.html"
    form_class = TreinadorForm
    success_url = "/"


class TreinadorDetailView(DetailView):
    model = Treinador
    template_name = "desafio/detalhes_treinador.html"
    context_object_name = "treinador"
    success_url = "/"


class PokemonCreateView(CreateView):
    model = Pokemon
    template_name = "desafio/pokemon_form.html"
    form_class = PokemonForm
    success_url = "/"


class PokemonUpdateView(UpdateView):
    model = Pokemon
    template_name = "desafio/pokemon_form.html"
    form_class = PokemonForm
    success_url = "/"
