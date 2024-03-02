from django.urls import path, include
from . import views

app_name = "desafio"

urlpatterns = [
    # path('', views.index, name='index'),
    path("api/", include("apps.desafio.api.urls")),
    path(
        "app/criar_treinador/",
        views.TreinadorCreateView.as_view(),
        name="criar_treinador",
    ),
    path(
        "app/ver_treinador/<int:pk>",
        views.TreinadorDetailView.as_view(),
        name="ver_treinador",
    ),
    path(
        "app/atualizar_treinador/<int:pk>",
        views.TreinadorUpdateView.as_view(),
        name="atualizar_treinador",
    ),
    path(
        "app/criar_pokemon/",
        views.PokemonCreateView.as_view(),
        name="criar_pokemon",
    ),
    path(
        "app/atualizar_pokemon/<int:pk>",
        views.PokemonUpdateView.as_view(),
        name="atualizar_pokemon",
    ),
]
