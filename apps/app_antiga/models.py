from django.db import models

# Create your models here.

class Teste(models.Model):
    descricao = models.TextField()

class RegistroUsuarios(models.Model):
    name = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.DecimalField(decimal_places=2, max_digits=7)

    class Meta:
        db_table = "registro_usuarios"

    def __str__(self):
        return self.name