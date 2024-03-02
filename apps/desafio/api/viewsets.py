# Importa as classes dentro do arquivo .serializers.py que se encontra no mesmo nível de diretório (.)
from .serializers import TreinadorSerializer, PokemonSerializer
from rest_framework.viewsets import ModelViewSet
# Importa as classes dentro do arquivo .models.py que se dois níveis acima do diretório (..)
from ..models import Treinador, Pokemon
# Importa as classes de permissões e autenticações do rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Importa as classes de paginação do rest_framework
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import requests

class PaginacaoPadrao(PageNumberPagination):
    page_size = 5 # Quantidade de itens por página
    page_size_query_param = 'tam_pagina' # Parâmetro para definir a quantidade de itens por página
    max_page_size = 50 # Quantidade máxima de itens por página

class TreinadorViewSet(ModelViewSet):
    '''Viewset Simples pra um CRUD de Treinadores'''
    # Lembrando que permissões e autenticações precisam ser do tipo tupla
    # Colocar apenas a permissão sem a vírgula, por exemplo, resultará em um erro
    # Pode ser colocada dentro de uma lista [IsAuthenticated] ou de uma tupla (IsAuthenticated,)

    permission_classes = (IsAuthenticated,)  # Permissão para acessar a API
    authentication_classes = (TokenAuthentication,)  # Autenticação por token
    queryset = Treinador.objects.all()
    serializer_class = TreinadorSerializer


class PokemonViewSet(ModelViewSet):
    '''Viewset Simples pra um CRUD de Pokemons baseado na Pokédex API'''
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    pagination_class = 
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def create(self, request, *args, **kwargs):
        '''Sobrescreve o método create para adicionar as informações da api de pokemons'''

        dados_da_requisicao = request.data
        nome_do_pokemon = dados_da_requisicao['nome']
        nome_do_pokemon_tratado = nome_do_pokemon.lower()
        # Faz a requisição para a API de pokemons

        url = f'https://pokeapi.co/api/v2/pokemon/{nome_do_pokemon_tratado}'
        resposta = requests.get(url)
        dados_do_pokemon = resposta.json()

        # Adiciona os dados da API na requisição
        treinador = dados_da_requisicao['treinador']
        # Pega o Nome do Pokemon
        nome = dados_do_pokemon.get('name', '')
        # Pega o Tipo do Pokemon
        tipos = dados_do_pokemon.get('types', [])
        tipo_pokemon = tipos[0]
        nome_do_tipo = tipo_pokemon.get('type', {}).get('name', '')
        # Pega os Ataques do Pokemon
        ataques = dados_do_pokemon.get('abilities', [])
        # Pega o nome do ataque 1
        ataque_1_json = ataques[0]
        nome_do_ataque_1 = ataque_1_json.get('ability', {}).get('name', '')
        # Pega o nome do ataque 2
        ataque_2_json = ataques[1]
        nome_do_ataque_2 = ataque_2_json.get('ability', {}).get('name', '')

        serializer = PokemonSerializer(data={'treinador': treinador, 'nome': nome, 'tipo': nome_do_tipo,
                                             'ataque_1': nome_do_ataque_1, 'ataque_2': nome_do_ataque_2})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
