from django.db import models

from apps.funcionarios.models import Funcionario

# Create your models here.
class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT) #evita que se remova funcionário logo após remover o documento
    
    def __str__(self):
        return self.descricao