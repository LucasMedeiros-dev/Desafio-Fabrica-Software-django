from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from .models import Treinador, Pokemon
from django.urls import reverse_lazy
import requests
# Create your views here.

# View Para Criação de Conta.


class CriarContaView(CreateView):
    template_name = 'desafio/criar_conta.html'
    success_url = reverse_lazy('desafio:login')
    # Define o modelo que será utilizado
    model = User
    # Define os campos que serão utilizados
    fields = ['username', 'password']


class CriarTreinadorView(CreateView):
    template_name = 'desafio/criar_treinador.html'
    success_url = reverse_lazy('desafio:criar_pokemon')
    # Define o modelo que será utilizado
    model = Treinador
    # Define os campos que serão utilizados
    fields = ['usuario', 'nome', 'idade']


class CriarPokemonView(CreateView):
    template_name = 'desafio/criar_pokemon.html'
    # Define o modelo que será utilizado
    model = Pokemon
    # Define os campos que serão utilizados
    fields = ['treinador', 'nome']

    def form_valid(self, form):
        # Recebe os dados do formulário
        treinador = form.cleaned_data['treinador']
        nome = form.cleaned_data['nome']
        # Trata o nome para garantir que ele sempre funcione
        nome_tratado = nome.lower()

        # Faz a requisição para a API de pokemons
        url = f'https://pokeapi.co/api/v2/pokemon/{nome_tratado}'
        resposta = requests.get(url)
        dados_do_pokemon = resposta.json()
        # Recebe os dados via Json e os trata
        nome = dados_do_pokemon.get('name', '')
        tipos = dados_do_pokemon.get('types', [])
        tipo_pokemon = tipos[0]
        nome_do_tipo = tipo_pokemon.get('type', {}).get('name', '')
        ataques = dados_do_pokemon.get('abilities', [])
        ataque_1_json = ataques[0]
        nome_do_ataque_1 = ataque_1_json.get('ability', {}).get('name', '')
        ataque_2_json = ataques[1]
        nome_do_ataque_2 = ataque_2_json.get('ability', {}).get('name', '')
        # Lembrando que aqui pode dar erro mesmo, pois a API pode não retornar os dados esperados
        # A inteção é que o aluno veja que é possível fazer requisições para APIs externas
        # Mesmo que dê erro se ele digar algo errado.

        # Altera na instância do formulário os valores que foram buscados na API
        form.instance.treinador = treinador
        form.instance.nome = nome
        form.instance.tipo = nome_do_tipo
        form.instance.ataque_1 = nome_do_ataque_1
        form.instance.ataque_2 = nome_do_ataque_2
        return super().form_valid(form)

    # Redireciona para a página de detalhes do pokemon
    def get_success_url(self):
        return reverse_lazy('desafio:pokemon_detail', kwargs={'pk': self.object.pk})


class PokemonDetailView(DetailView):
    template_name = 'desafio/pokemon.html'
    model = Pokemon
    context_object_name = 'pokemon'
