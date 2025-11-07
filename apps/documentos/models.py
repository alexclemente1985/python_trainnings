from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario

# Create your models here.
class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT) #evita que se remova funcionário logo após remover o documento
    arquivo = models.FileField(upload_to='documentos')

    # Informa para aonde a aplicação será redirecionada após o envio do formulário, atualizando o funcionário dono do documento
    def get_absolute_url(self):
        print(f'get absolute url pertence.id-> {self.pertence.id}')
        return reverse("update_funcionario", args=(self.pertence.id,)) #args precisa ser iteravel... a vírgula no final alerta ao python que o parênteses é uma tupla
    

    def __str__(self):
        return self.descricao