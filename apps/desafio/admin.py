from django.contrib import admin
# Importa os modelos Treinador e Pokemon que estão no mesmo nível de diretório (.)
from .models import Treinador, Pokemon
# Register your models here.

# Registra os modelos Treinador e Pokemon no admin


@admin.register(Treinador)
class TreinadorAdmin(admin.ModelAdmin):
    pass


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

# Ou

# admin.site.register(Treinador)
# admin.site.register(Pokemon)
