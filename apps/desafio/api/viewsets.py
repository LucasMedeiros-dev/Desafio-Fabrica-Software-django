# Importa as classes dentro do arquivo .serializers.py que se encontra no mesmo nível de diretório (.)
from .serializers import TreinadorSerializer, PokemonSerializer
from rest_framework.viewsets import ModelViewSet
# Importa as classes dentro do arquivo .models.py que se dois níveis acima do diretório (..)
from ..models import Treinador, Pokemon


class TreinadorViewSet(ModelViewSet):
    queryset = Treinador.objects.all()
    serializer_class = TreinadorSerializer


class PokemonViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
