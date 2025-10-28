import re
from validate_docbr import CPF

def cpf_invalido(cpf):
    if not CPF().validate(cpf):
        return len(cpf) != 11

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    # return len(celular) != 13
    return resposta