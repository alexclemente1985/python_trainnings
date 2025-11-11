import io
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, TemplateView
from .models import Funcionario
from django.contrib.auth.models import User

#reportlab
from reportlab.pdfgen import canvas

#xhtml2pdf
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

from pathlib import Path

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

class RenderXhtml2pdf:
    #função que será chamada sempre que precisar gerar o relatório
    @staticmethod
    def render(path: str, params:dict, filename:str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")),
            response
        )

        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), 
                content_type='application/pdf'
            )
            response['Content-Disposition'] = 'attachment; filename="%s.pdf"'%filename
            return response
        else:
            return HttpResponse("Error rendering PDF", status=400)

# para ser chamada na tela e gerar o pdf xhtml2pdf
class Xhtml2pdf(View):
    def get(self, request):
        # Necessário mandar url completa para achar -> alterar para porta Nginx no server
        params = {
            'sales': 'Variavel sales',
            'background': 'http://localhost:8000/media/documentos/carina-nebula.png', 
            'request': request
        }

        return RenderXhtml2pdf.render('funcionarios/relatorio.html', params, 'xhtml2pdf_report')
    

# Para realizar debugs
class Xhtml2pdfDebug(TemplateView):
    template_name = 'funcionarios/relatorio_debug.html'
    print(Path.joinpath( Path.cwd().parents[1],'/static/media/documentos/carina-nebula.png'))
    
    def get(self, request):
        params = {
            'sales': 'Variavel sales',
            'background': '/media/documentos/carina-nebula.png',
            
        }
      #  return render(request,'funcionarios/relatorio_debug.html',params)

        return RenderXhtml2pdf.render('funcionarios/relatorio_debug.html', params, 'xhtml2pdf_report')