from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.contrib.auth.models import User

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
    

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        
        funcionario = form.save(commit=False) #permite criar o objeto apenas em memória, devido à mudanças futuras
        funcionario.empresa = self.request.user.funcionario.empresa

        username = funcionario.nome.split(' ')[0]+funcionario.nome.split(' ')[1]

        funcionario.user = User.objects.create(username=username)

        funcionario.save()

        return super(FuncionarioCreate, self).form_valid(form)