from django.contrib.auth.models import User
from apps.desafio.models import Treinador


def create_user_choices():
    data = []
    try:
        for user in User.objects.all():
            # adiciona tupla com id e username do usuário ao fim da lista
            data.append((user.id, user.username))
    except Exception:
        # retorna "None" caso ocorra algum erro
        return [("None", "None")]

    # retorna os dados ou "None" caso não haja usuários
    return data or [("None", "None")]


def create_trainer_choices():
    data = []
    try:
        for treinador in Treinador.objects.all():
            # adiciona tupla com id e username do treinador ao fim da lista
            data.append((treinador.id, treinador.nome))
    except Exception:
        # retorna "None" caso ocorra algum erro
        return [("None", "None")]

    # retorna os dados ou "None" caso não haja usuários
    return data or [("None", "None")]
