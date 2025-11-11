import io
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.contrib.auth.models import User
from reportlab.pdfgen import canvas

# Create your views here.

class FuncionariosList(ListView):
    model = Funcionario

    #função padrão do Django para buscas 
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa

        #IMPORTANTE: esse método permite que apenas sejam retornados funcionários que estejam na mesma empresa do funcionário logado
        print(Funcionario.objects.filter(empresa=empresa_logada))
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
    
def pdf_reportlab_funcionarios(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 810, 'Relatório de Funcionários')
    
    p.drawString(0, 800, '_'*150)

    y=750 #inicia o relatório um pouco mais abaixo que o título acima (quanto maior y, mais alto no documento)

    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa).all()
    
    str_ = 'Nome: %s | Horas Extras: %s'

    for funcionario in funcionarios:
        if funcionario.total_horas_extra == None:
            horas = "0 h"
        else:
            horas = f'{funcionario.total_horas_extra} h'
        p.drawString(100,y,str_%(funcionario.nome, horas)) #STRING + % + (tupla) -> maneira de criar strings formatadas (string tem que ter parâmetros com %)
        y-=20

    


    # palavras = ['palavra1','palavra2','palavra3']

    # y=790

    # for palavra in palavras:
    #     p.drawString(10,y,palavra)
    #     y-=40

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response