import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
import xlwt

from apps.registro_hora_extra.forms import RegistroHoraExtraForm
from apps.registro_hora_extra.models import RegistroHoraExtra

# Create your views here.

class HoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    # Importante para enviar os dados do usuário logado para o formulário de horas extras
    def get_form_kwargs(self):
        kwargs = super(HoraExtraNovo, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa

        return self.model.objects.filter(funcionario__empresa=empresa_logada)
    
class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm #permite usar o formulário customizado ao invés do padrão do Django

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
    
class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    # success_url = reverse_lazy('update_hora_extra_base')

    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
    
class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class ExportarCSV(View):
    model = RegistroHoraExtra
    def get_success_url(self):
        return reverse_lazy('list_hora_extra')
    
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="horas_extras.csv"'

        writer = csv.writer(response)
        
        empresa_logada = self.request.user.funcionario.empresa
        horas = self.model.objects.filter(funcionario__empresa=empresa_logada)

        writer.writerow(['Motivo','Funcionário','Horas Restantes', 'Horas Retiradas'])
        for hora in horas:
            writer.writerow([hora.motivo, hora.funcionario.nome, hora.funcionario.total_horas_extra, hora.horas])
        

        return response

class ExportarExcel(View):
    model = RegistroHoraExtra

    def get_success_url(self):
        return reverse_lazy('list_hora_extra')
    
    def get(self, request):
        response = HttpResponse(content_type='text/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="horas_extras.xls"'

        writerB = xlwt.Workbook(encoding="utf-8")
        writerS = writerB.add_sheet('Funcionários')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id','Motivo','Funcionário', 'Horas Extras']

        for col_num in range(len(columns)):
            writerS.write(row_num, col_num, columns[col_num], font_style)
        
        font_style = xlwt.XFStyle()

        empresa_logada = self.request.user.funcionario.empresa
        horas = self.model.objects.filter(funcionario__empresa=empresa_logada)

        row_num = 1

        for hora in horas:
            writerS.write(row_num, 0, hora.id, font_style)
            writerS.write(row_num, 1, hora.motivo, font_style)
            writerS.write(row_num, 2, hora.funcionario.nome, font_style)
            writerS.write(row_num, 3, hora.horas, font_style)

            row_num += 1
        
        writerB.save(response)
        

        return response