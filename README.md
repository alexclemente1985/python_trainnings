# README

## Informações Úteis

### Criando ambiente virtual venv manualmente (pasta raiz do projeto):
`python3 -m venv .venv`

### Ativando o ambiente virtual criado:
- macOS/Linux:
  `source .venv/bin/activate`
- Windows:
  `.venv\Scripts\activate`

### Verificando a ativação do ambiente virtual
- macOS/Linux:
  `which python`
- Windows:
  `where python`

### Caminho para o python do venv:
- macOS/Linux:
  `.venv/bin/python`
- Windows:
  `.venv\Scripts\python`

### Desativando o ambiente virtual venv
`deactivate`

### Instalando libs a partir de requirements.txt:
`pip install -r requirements.txt`

### Criando arquivo de requirements.txt a partir das libs já instaladas:
`pip freeze > requirements.txt`

### Instalando Django
`pip install django`

### Criando projeto Django
`django-admin startproject <nome_do_projeto> .`

### Criando app Django
`python3 manage.py startapp <NOME_APP>`
- Integrar o projeto em settings -> installed apps (escrever o nome do app na lista)

### Rodando o server Django
- Iniciar o arquivo gerado pelo comando anterior
`python3 manage.py runserver` ou `python manage.py runserver`

### Acessando o django admin
`django-admin startproject <nome_do_projeto>`

### Criação de tabelas
`python3 manage.py makemigrations`

### Alimentação do banco de dados com as migrations
`python3 manage.py migrate`

### Django shell
`python3 manage.py shell`

### Criação de superuser para admin Django
`python3 manage.py createsuperuser`

### Registro das tabelas no admin
- Necessário registrar as tabelas no arquivo admin.py do app criado
- No arquivo:
-- Importar os models (arquivo models.py): `from .models import <NOME_CLASSE_EM_MODELS.PY>`
-- Fazer o registro da tabela: `admin.site.register(<NOME_MODEL>,<NOME_CLASSE_ADMIN>)`

### Biblioteca Faker (para dados fictícios para testes)
`pip install faker`

### Recolocação da SECRET_KEY em arquivo .env
- adicionar python-dotenv
`pip install python-dotenv`
- Criar arquivo `.env` na pasta raiz e criar variável de mesmo nome com valor sem aspas
- em projeto -> settings.py, ir na variável e substituir o valor por `srt(os.getenv('SECRET_KEY'))` (`os` vem de `import os`)
- em projeto -> settings.py, chamar a função `load_dotenv()` no início, fazendo `from dotenv import load_dotenv`

### Documentação do projeto
`pip install drf-yasg`
- adicionar o app `drf_yasg` em settings.py -> INSTALLED_APPS

### Acesso à documentação pelo Swagger
`localhost:<porta>/swagger`

### Acesso à documentação pelo Redoc
`localhost:<porta>/redoc`

### Rodando o server na hospedagem Linux
- Confirmar a instalação do python 3 e pip
`sudo apt install python3 python3-pip python3-venv`
- ASGI Server -> uvicorn (instalação)
`pip install uvicorn[standard]`
- Rodar na porta 8000
`python manage.py runserver 0.0.0.0:8000`

### Testes no server DRF
#### Verificação com curl
`curl -u <usuario_API>:<senha_usuario_API> http://localhost:8000/`

### DJANGO
#### Uso de arquivos estáticos (styles e assets)
- criar dentro do projeto a pasta `static`
- criar as pastas `assets` e `styles` e colocar as imagens e estilos css, respectivamente
- em projeto -> settings.py, inserir as seguintes informações abaixo de `STATIC_URL`:

```
STATIC_URL = 'static/'

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'setup/static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

- Após, rodar o comando `python3 manage.py collectstatic` para o Django poder encontrar os arquivos corretamente

#### Atualização do template para uso dos arquivos estáticos
- Após sequência anterior, adicionar o código `{% load static %}` na primeira linha do arquivo .html de template
- Em cada referência a um arquivo estático, ao longo do html, deve-se usar `{% static '<caminho_arquivo_estático>' %}` para fazer os carregamentos na tela.

#### Atualização de arquivos de app
- Em `INSTALLED_APPS`, colocar como app a função presente em `<app> -> apps.py -> <APP>Config`
`<nome_app>.apps.<nome_app>Config`
- Isto permitirá atualizações de todos os arquivos e configurações do app

#### Uso de ImageField em models
- necessário importa lib `Pillow`
`pip install Pillow`

#### Apps CORE
- Usado para centralizar chamadas padrão
- Recomendação: usar a seguinte estrutura para templates do core `apps -> core -> templates -> core -> <NOME_TEMPLATE>.html`

#### Django e Bootstrap
- Em caso de problemas com módulo `distutils` (removido após python v3.12): `pip install --upgrade setuptools`

#### Django e arquivos estáticos
- o Django, no modo produção (`DEBUG = False` em `settings.py`), não provê os arquivos estáticos (como arquivos css e js)
- Para que possa prover, é necessário ou configurar um Ngnix para serví-los ou rodar o comando `python3 manage.py runserver --insecure` (indicado apenas para hospedagem local)
- **NOTA**: mesmo com a configuração `--insecure`, arquivos de mídia (_imagens, etc._) **NÃO** serão servidos pelo Django, devendo-se realizar uma configuração a parte no Ngnix ou Apache.
- **NOTA 2:** é uma boa prática criar pastas `static/<nome_app>` em cada pasta de app no caso de existirem arquivos estáticos particulares, pois o Django varre toda a aplicação procurando pastas `static` e, com o comando `collectstatic`, irá organizar tudo na pasta definida em `STATIC_ROOT`.





http://localhost:8000/media/documentos/Modal.png
http://localhost:8000/media/documentos/carina-nebula.png