from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_cpf, validate_nome, validate_celular
# Create your models here.


class Estudante(models.Model):

    # Necessário para se obter validação customizada no admin... serializer só pega no DRF
    nome = models.CharField(max_length=100, validators=[validate_nome])
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11, unique=True, validators=[validate_cpf]) 
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14, validators=[validate_celular])

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(3)])
    descricao = models.CharField(max_length=100, blank = False)
    nivel = models.CharField(max_length=1, blank=False, null=False, default='B')

    def __str__(self):
        return self.codigo

# Relacionamento many-to-one
class Matricula(models.Model):
    PERIODO = (
        ('M','Matutino'),
        ('V','Vespertino'),
        ('N','Noturno'),
    )
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')