import re
from validate_docbr import CPF

from django.core.exceptions import ValidationError

def validate_cpf(value):
    cpf = CPF()
    if not cpf.validate(value):
    # if len(value) != 11:
        raise ValidationError('CPF tem que ter valor válido')

def validate_nome(nome):
    if not nome.isalpha():
        raise ValidationError('O nome só pode ter letras')

def validate_celular(celular):
    # if len(celular) != 13:
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    if len(resposta)==0:
        raise ValidationError('Valor inválido para celular')
        