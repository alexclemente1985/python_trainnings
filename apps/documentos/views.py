from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from apps.documentos.models import Documento


# Create your views here.
class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # def form_valid(self, form):
    #     documento = form.save(commit=False)
    #     pertence = self.request.user.funcionario
    #     return super().form_valid(form)

class DocumentoEdit(UpdateView):
    pass


class DocumentoDelete(DeleteView):
    pass

class DocumentosList(ListView):
    pass