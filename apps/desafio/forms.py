from django import forms

from .models import Treinador, Pokemon
from django.contrib.auth.models import User
from .utils.create_selects import create_user_choices, create_trainer_choices


class TreinadorForm(forms.ModelForm):
    """Formulário para inserção e atualização de Treinador"""

    class Meta:
        model = Treinador
        fields = (
            "usuario",
            "nome",
            "idade",
        )
        widgets = {
            "usuario": forms.Select(choices=create_user_choices()),
        }


class PokemonForm(forms.ModelForm):
    """Formulário para inserção e atualização de Pokemon"""

    class Meta:
        model = Pokemon
        fields = (
            "treinador",
            "nome",
        )
        widgets = {
            "usuario": forms.Select(choices=create_trainer_choices()),
        }
