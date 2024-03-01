from rest_framework.serializers import ModelSerializer
# os dois pontos referenciam dois diretórios acima do arquivo atual /api e /desafio
from ..models import Treinador, Pokemon


class TreinadorSerializer(ModelSerializer):
    class Meta:
        model = Treinador
        fields = ["id", "usuario", "nome", "idade"]


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ["id", "treinador", "nome", "tipo", "ataque_1", "ataque_2"]
