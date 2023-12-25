# Timesheet

Um simples sistema de controle de ponto eletrônico para resolver o meu problema de geral um pdf automaticamente ao fim do mês 😄.

## Como usar localmente

```shell
git clone https://github.com/henriquesebastiao/timesheet.git
cd timesheet
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Defina a variável de ambiente `DEBUG` como `1` para rodar o servidor em modo de desenvolvimento com um banco de dados SQLite.

```shell
export DEBUG=1
```

```shell
python manage.py migrate
```

Crie um super usuário para acessar o painel de administração.

```shell
python manage.py createsuperuser
```

Rode o servidor de desenvolvimento.

```shell
python manage.py runserver
```

Acessar o painel de administração em `http://localhost:8000/` e entrar com o usuário criado anteriormente.