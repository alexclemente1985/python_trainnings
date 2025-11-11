from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse #permite usar os recursos de autenticação do Django
from django.db.models import Avg, Count, Min, Sum

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.PROTECT, unique=True) #Permite que primeiro se delete o funcionário e depois o usuário
    user = models.OneToOneField(User, on_delete=models.PROTECT) # garante que exista apenas um único funcionário para cada usuário
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self): #redireciona para lista de funcionários após o update do funcionário
        return reverse("list_funcionarios")
    
    @property
    def total_horas_extra(self):
        return self.registrohoraextra_set.all().aggregate(Sum('horas'))['horas__sum'] #registrohoraextra_set se encontra presente por meio do relacionamento criado pelo django
    

    def __str__(self):
        return self.nome
    
