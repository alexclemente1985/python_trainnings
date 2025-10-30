from django.contrib import admin
from .models import Fotografia

# Register your models here.
class FotografiasAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'legenda','categoria', 'descricao', 'foto', 'publicada', 'data_fotografia']
    search_fields = ['nome', 'categoria']
    list_filter = ['nome', 'categoria', 'publicada']
    list_display_links = ("id","nome")
    # paginação
    list_per_page = 1
    # elemento editável (tem que deixar sempre como tupla -> terminar com "," se for só um campo)
    list_editable = ('publicada',)
    # ordenação
    


admin.site.register(Fotografia, FotografiasAdmin)
