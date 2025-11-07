from django.urls import path
from .views import DocumentoCreate, DocumentoDelete, DocumentoEdit, DocumentosList

urlpatterns = [
    path('novo/<int:funcionario_id>', DocumentoCreate.as_view(), name='create_documento'),
    # path('editar/<int:pk>', DocumentoEdit.as_view(), name='update_documento'),
    # path('deletar/<int:pk>', DocumentoDelete.as_view(), name='delete_documento')
]
