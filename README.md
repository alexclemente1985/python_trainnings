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

#### Criando com arquivo .spec

- Gerando arquivo .spec: `pyi-makespec --onefile --windowed <nome_arquivo>.py`

- Editando arquivo .spec:

`# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['<nome_arquivo>.py'],
    pathex=[],  # Add paths if needed
    binaries=[],
    datas=[],  # Add data files if needed
    hiddenimports=['PySide6'],  
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt5', 'PySide2', 'PyQt6'],  
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='YourAppName',  # Set the name of your executable
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set console to False
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='path/to/your/icon.ico'  # Replace 'path/to/your/icon.ico' with the path to your icon file
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='<nome_arquivo>',
)`

- Criando o executável: `pyinstaller <nome_arquivo>.spec`

_Informações obtidas de <https://github.com/KhamisiKibet/24-Modern-Desktop-GUI>_

#### Possíveis problemas na criação do executável

- Uso de PyQT6 junto com PySide6 pode impedir criação do .exe       (remover PyQT6)
  - _Solução: remover PyQT6_ `pip uninstall PyQT6`


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
