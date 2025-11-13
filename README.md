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


#### Django e uWSGI
- Em produção, tem que usar o uWSGI (ou aWSGI) no lugar do server padrão de desenvolvimento
1. Criar venv na pasta do projeto no server de produção
- `python3 -m venv .venv`
2. Ativar venv
- `source .venv/bin/activate`
3. Instalar o uWSGI
- `pip install uwsgi`
4. Executar o comando para rodar o projeto no uwsgi:
- `uwsgi --http :8000 --module <NOME_PROJETO>.wsgi`

#### Django, gunicorn e NGnix
- Webserver para conexão do browser com o uWSGI
1. Instalar o NGnix no server
- `sudo apt-get install nginx`
2. Com a venv ativa, instalar e testar o gunicorn
- `pip install gunicorn`
- `gunicorn --bind 0.0.0.0:<PORTA> <PROJETO>.wsgi:application`

3. Ir na pasta do nginx `sites-available` e criar o arquivo `<nome_projeto>.conf`
- `cd /etc/nginx/sites-available/`

4. Salvar o seguinte conteúdo no arquivo de configuração (mudar caminhos de media, static e include do location para o caminho da pasta do projeto django -> executar comando `pwd` no interior da pasta e copiar caminho)
- **NOTA:** Configuração abaixo não contempla execução do gunicorn via systemctl
```
server {
        listen <PORTA QUE DESEJA ABRIR>;
        server_name localhost; # Your domain or IP
        client_max_body_size 100M;

        location = /favicon.ico { access_log off; log_not_found off; }
        location /static/ {
            root /PASTA/QUE/CONTEM/PASTA/DE/ARQUIVOS/ESTÁTICOS;; # Your project directory
        }

        location /media/ {
            root /PASTA/QUE/CONTEM/PASTA/DE/ARQUIVOS/DE/MEDIA;
        }

        
        location / {
            include proxy_params;
            proxy_pass http://localhost:<PORTA QUE DESEJA RODAR O PROJETO>;
           # proxy_pass http://unix:/run/gunicorn.sock;
        }
```

5. Criar link simbólico para o arquivo dentro da pasta `sites-enabled` de `/etc/nginx`
- `sudo ln -s /etc/nginx/sites-available/<NOME DO ARQUIVO DO PROJETO SEM EXTENSÃO> /etc/nginx/sites-enabled/`

6. Verificar se o link simbólico foi criado executando o seguinte comando na pasta `sites-enabled` (verificar aparecimento do nome do arquivo na cor azulada ou em outra que não seja vermelha):
- `ls -la /etc/nginx/sites-enabled/`

7. Testar o Nginx e reiniciar se tudo estiver ok:
- `sudo nginx -t`
- `sudo nginx -s reload `

8. Adicionar a configuração do STATIC_ROOT para ao projeto, caso não tenha ainda feito
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static') 
```

9. Executar o comando para coleta de arquivos estáticos na pasta da aplicação
- `python3 manage.py collectstatic`

10. Inicializar o gunicorn na pasta do projeto
- `gunicorn --bind 0.0.0.0:<PORTA> <PROJETO>.wsgi:application`

#### Django Rest Framework e Autenticação de apps clientes
- Caso esteja usando o módulo `authtoken`, deve-se realizar um `migrate` após sua instalação em `settings.py`, e depois gerar um token para o usuário da aplicação no painel admin do django
- Usar o token criado na aplicação cliente, no Header `Authorization` com valor `Token <TOKEN GERADO>`

#### Múltiplos bancos de dados
1. Adicionar as configurações do banco no arquivo `settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    '<OUTRO_BANCO>':{
        'ENGINE': '<ENGINE.DO.BANCO>',
        'NAME': BASE_DIR / '<NOME DO BANCO>.<EXTENSÃO>',
    }
}
``` 
2. Criar a aplicação do projeto que irá acessar o banco
- `python3 manage.py startapp <NOVA_APLICAÇÃO_BANCO>`

3. Inserir a nova aplicação em `INSTALLED_APPS` de `settings.py`

3. Criar os modelos desejados para a aplicação, registrar no admin e realizar `python3 manage.py makemigrations`

4. Criar arquivo `DBRoutes.py` dentro da pasta do projeto, e criar a seguinte classe:

```
class DBRoutes:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == '<NOVA_APLICAÇÃO_BANCO>':
            return '<OUTRO_BANCO>'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label == '<NOVA_APLICAÇÃO_BANCO>':
            return '<OUTRO_BANCO>'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == '<NOVA_APLICAÇÃO_BANCO>' or \
           obj2._meta.app_label == '<NOVA_APLICAÇÃO_BANCO>':
           return True
        return None
    
    def allow_migrate(self, db, app_label, mmodel_name=None, **hints):
        if app_label == '<NOVA_APLICAÇÃO_BANCO>':
            return db == '<OUTRO_BANCO>'
        return None
    
```
5. Inserir em `settings.py` o seguinte trecho:
```
DATABASE_ROUTERS = ['<PASTA_PROJETO>.DBRoutes.DBRoutes']
```

6. Executar comando `python3 manage.py migrate --database=<OUTRO_BANCO>`

**NOTA:** Para cada banco de dados deve-se criar um arquivo "DBRoutes" diferente (boa prática) e inserir em `DATABASE_ROUTERS` no `settings.py`


7. Para acessar os dados do outro banco, de maneira manual
`MODEL.objects.using('<OUTRO_BANCO>').<COMANDO>`
- Para o caso de alterações em instâncias de Models
`MODEL.objects.save(using='<BANCO>')` 
`MODEL.objects.delete(using='<OUTRO_BANCO>')`