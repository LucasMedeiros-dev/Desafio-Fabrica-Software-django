# Desafio Django Fábrica

Este é um projeto Django com uma API simples para gerenciar treinadores e pokemons.

## Instalação

Primeiro, clone o repositório para sua máquina local:

```sh
git clone https://github.com/LucasMedeiros-dev/Desafio-F-brica-2.0.git
```

Navegue até o diretório do projeto:

```sh
cd Desafio-F-brica-2.0
```

Instale os pacotes necessários usando pip:

```sh
pip install -r requirements.txt
```

## Executando o Servidor

Para iniciar o servidor Django, execute o seguinte comando:

```sh
python manage.py runserver
```

O servidor será iniciado em `http://127.0.0.1:8000/`.

## Endpoints

Os seguintes endpoints estão disponíveis:

- `admin/`: Site de administração do Django.
- `api/treinadores/`: Endpoint da API para gerenciar treinadores. Suporta `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
- `api/pokemons/`: Endpoint da API para gerenciar pokemons. Suporta `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.

Cada um desses endpoints é definido em [`apps/desafio/api/urls.py`](command:_github.copilot.openSymbolInFile?%5B%22apps%2Fdesafio%2Fapi%2Furls.py%22%2C%22apps%2Fdesafio%2Fapi%2Furls.py%22%5D "apps/desafio/api/urls.py") e manipulado por viewsets em [`apps/desafio/api/viewsets.py`](command:_github.copilot.openSymbolInFile?%5B%22apps%2Fdesafio%2Fapi%2Fviewsets.py%22%2C%22apps%2Fdesafio%2Fapi%2Fviewsets.py%22%5D "apps/desafio/api/viewsets.py").

