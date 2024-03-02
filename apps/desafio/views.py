import requests

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.models import User

from .forms import TreinadorForm, PokemonForm
from .models import Treinador, Pokemon


# view para criar conta
class CriarContaView(CreateView):
    template_name = "desafio/criar_conta.html"
    success_url = reverse_lazy("desafio:login")
    # Define o modelo que será utilizado
    model = User
    # Define os campos que serão utilizados
    fields = ["username", "password"]


# ===== TREINADORES =====
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


# ===== POKEMONS =====
class PokemonCreateView(CreateView):
    template_name = "desafio/pokemon_form.html"
    # Define o modelo que será utilizado
    model = Pokemon
    # Define os campos que serão utilizados
    fields = ["treinador", "nome"]

    def form_valid(self, form):
        # Recebe os dados do formulário
        treinador = form.cleaned_data["treinador"]
        nome = form.cleaned_data["nome"]
        # Trata o nome para garantir que ele sempre funcione
        nome_tratado = nome.lower()

        # Faz a requisição para a API de pokemons
        url = f"https://pokeapi.co/api/v2/pokemon/{nome_tratado}"
        resposta = requests.get(url)
        dados_do_pokemon = resposta.json()
        # Recebe os dados via Json e os trata
        nome = dados_do_pokemon.get("name", "")
        tipos = dados_do_pokemon.get("types", [])
        tipo_pokemon = tipos[0]
        nome_do_tipo = tipo_pokemon.get("type", {}).get("name", "")
        ataques = dados_do_pokemon.get("abilities", [])
        ataque_1_json = ataques[0]
        nome_do_ataque_1 = ataque_1_json.get("ability", {}).get("name", "")
        ataque_2_json = ataques[1]
        nome_do_ataque_2 = ataque_2_json.get("ability", {}).get("name", "")

        # Altera na instância do formulário os valores que foram buscados na API
        form.instance.treinador = treinador
        form.instance.nome = nome
        form.instance.tipo = nome_do_tipo
        form.instance.ataque_1 = nome_do_ataque_1
        form.instance.ataque_2 = nome_do_ataque_2
        return super().form_valid(form)

    # Redireciona para a página de detalhes do pokemon
    def get_success_url(self):
        return reverse_lazy("desafio:pokemon_detail", kwargs={"pk": self.object.pk})


class PokemonDetailView(DetailView):
    template_name = "desafio/pokemon.html"
    model = Pokemon
    context_object_name = "pokemon"


class PokemonUpdateView(UpdateView):
    model = Pokemon
    template_name = "desafio/pokemon_form.html"
    form_class = PokemonForm
    success_url = "/"
