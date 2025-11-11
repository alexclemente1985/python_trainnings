from django.urls import path
from apps.funcionarios.views import FuncionariosList, FuncionarioEdit, FuncionarioDelete, FuncionarioCreate, pdf_reportlab_funcionarios, Xhtml2pdf, Xhtml2pdfDebug


urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo/', FuncionarioCreate.as_view(), name='create_funcionario'),
    path('editar/<int:pk>', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('pdf-reportlab', pdf_reportlab_funcionarios, name='pdf_reportlab_funcionario'),
    path('pdf-xhtml2pdf', Xhtml2pdf.as_view(), name='pdf_xhtml2pdf_funcionario'),
    path('pdf-xhtml2pdf-debug', Xhtml2pdfDebug.as_view(), name='pdf_xhtml2pdf_funcionario_debug')
]
