from django.contrib import admin

from apps.app_antiga.models import RegistroUsuarios, Teste

class RegistroUsuarioAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return RegistroUsuarios.objects.using("antigo").all()

# Register your models here.
admin.site.register(Teste)
admin.site.register(RegistroUsuarios, RegistroUsuarioAdmin)