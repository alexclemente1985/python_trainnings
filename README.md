# README

## Informações para desenvolvimento QT Designer

### Acesso ao QT Designer do PySide6
-Na pasta desejada, digitar no terminal: `pyside6-designer`

### Conversão de arquivo .ui em .py no PySide6

-`pyside6-uic <nome_arquivo>.ui -o <nome_arquivo>.py`

### Conversão de arquivo .qrc em .py no PySide6 (imagens, ícones, etc.)
-`pyside6-rcc <nome_arquivo>.qrc -o <nome_arquivo>.py`

#### Uso das imagens do arquivo convertido
- Importar o arquivo .py no código do projeto `import <nome_arquivo_imagem_py>`
- Remover a importação `import <nome_arquivo_imagem>.rc`
- Mais informações, seguir instruções do site <https://doc.qt.io/qtforpython-6.5/tutorials/basictutorial/qrcfiles.html>

### Criação do executável
- Na pasta do arquivo principal (_arquivo único, sem console_): `pyinstaller --onefile --noconsole <nome_arquivo>.py`

## Informações para resolução de exercícios

### Libs atualizadas em relação às mostradas em aula
- **pycep_correios:** Agora é **brasilcep**; ver pacote em <https://pypi.org/project/brazilcep/>.

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
`pip3 install -r requirements.txt`

### Criando arquivo de requirements.txt a partir das libs já instaladas:
`pip freeze > requirements.txt`
`pip3 freeze > requirements.txt`
