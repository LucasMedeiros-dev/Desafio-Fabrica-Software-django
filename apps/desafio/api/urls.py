from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets
# No caso de api, é necessário criar um objeto do tipo DefaultRouter e registrar as views que serão utilizadas
router = DefaultRouter()
# Registra a viewset TreinadorViewSet
router.register('treinadores', viewsets.TreinadorViewSet)
# Registra a viewset PokemonViewSet
router.register('pokemons', viewsets.PokemonViewSet)

urlpatterns = [
    # Cadastra as urls do router
    path('', include(router.urls)),
]
