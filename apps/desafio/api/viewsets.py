# Importa as classes dentro do arquivo .serializers.py que se encontra no mesmo nível de diretório (.)
from .serializers import TreinadorSerializer, PokemonSerializer
from rest_framework.viewsets import ModelViewSet
# Importa as classes dentro do arquivo .models.py que se dois níveis acima do diretório (..)
from ..models import Treinador, Pokemon
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


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
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
