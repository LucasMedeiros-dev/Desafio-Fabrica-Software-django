from django.urls import path, include
from . import views

app_name = 'desafio'

urlpatterns = [
    # path('', views.index, name='index'),
    path('api/', include('apps.desafio.api.urls')),
]
