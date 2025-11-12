from django.urls import path

from apps.registro_hora_extra.views import ExportarCSV, ExportarExcel, HoraExtraDelete, HoraExtraEdit, HoraExtraEditBase, HoraExtraList, HoraExtraNovo
  

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo/', HoraExtraNovo.as_view(), name='create_registro_hora_extra'),
    path('editar-funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('editar/<int:pk>/', HoraExtraEditBase.as_view(), name='update_hora_extra_base'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('exportar-csv/', ExportarCSV.as_view(), name='exportar_csv'),
    path('exportar-excel/', ExportarExcel.as_view(), name='exportar_excel'),
]
