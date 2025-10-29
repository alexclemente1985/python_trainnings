from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from .serializer_validators import nome_invalido, cpf_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']

    def validate(self,dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter 11 dígitos!'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular':'O celular precisa ter 13 dígitos'})
        return dados
    
    # def validate_cpf(self,cpf):
    #     print("validando cpf...")
    #     if(len(cpf) != 11):
    #         print(f'cpf invalidado.... {cpf}')
    #         raise serializers.ValidationError('O CPF tem que ter 11 dígitos!')
    #     return cpf
    
    # def validate_nome(self, nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError('O nome só pode ter letras')
    #     return nome
    
    # def validate(self,celular):
    #     if len(celular) != 13:
    #         raise serializers.ValidationError('O celular precisa ter 13 dígitos')
    #     return celular

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields ='__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        # fields ='__all__'
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    
    class Meta:
        model = Matricula
        fields = ['estudante_nome']

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','celular']