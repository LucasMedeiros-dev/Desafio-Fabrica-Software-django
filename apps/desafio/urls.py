from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import LoginView
from . import views
app_name = 'desafio'

urlpatterns = [
    path('api/', include('apps.desafio.api.urls')),
    path('criar-conta/', views.CriarContaView.as_view(), name='criar_conta'),
    path('login/', LoginView.as_view(template_name='desafio/login.html'), name='login'),
    path('criar-treinador/', views.CriarTreinadorView.as_view(),
         name='criar_treinador'),
    path('criar-pokemon/', views.CriarPokemonView.as_view(),
         name='criar_pokemon'),
    path('pokemon/<int:pk>/', views.PokemonDetailView.as_view(),
         name='pokemon_detail'),
]
