from django import forms

from .models import Treinador, Pokemon


class TreinadorForm(forms.ModelForm):
    """Formulário para inserção e atualização de Treinador"""

    class Meta:
        model = Treinador
        fields = (
            "usuario",
            "nome",
            "idade",
        )


class PokemonForm(forms.ModelForm):
    """Formulário para inserção e atualização de Pokemon"""

    class Meta:
        model = Pokemon
        fields = (
            "treinador",
            "nome",
        )
