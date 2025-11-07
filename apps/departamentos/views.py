from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from apps.departamentos.models import Departamento
# Create your views here.

#Não se acrescenta ou edita 'empresa' pois esta será definida pela empresa do usuário

# O funcionamento das classes abaixo depende da existência dos templates com sufixos _list, _form e _confirm_delete
## pois usa recursos do django (django.views.generic)
class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa

        departamento.save()

        return super(DepartamentoCreate, self).form_valid(form)
    

class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ['nome']

class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')

class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)