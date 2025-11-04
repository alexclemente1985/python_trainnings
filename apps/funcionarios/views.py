from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Funcionario

# Create your views here.

class FuncionariosList(ListView):
    model = Funcionario

    #função padrão do Django para buscas 
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa

        #IMPORTANTE: esse método permite que apenas sejam retornados funcionários que estejam na mesma empresa do funcionário logado
        return Funcionario.objects.filter(empresa=empresa_logada)
    
class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')
    