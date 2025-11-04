from django.urls import path
from apps.core.views import home
from apps.empresas.views import EmpresaCreate, EmpresaEdit


urlpatterns = [
    path('novo',EmpresaCreate.as_view(), name="create_empresa"),
    path('editar/<int:pk>',EmpresaEdit.as_view(), name="edit_empresa"), #Importante passar o 'pk' pois o id vem do banco e já é repassado na url
]
