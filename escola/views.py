# from django.shortcuts import render
from django.http import JsonResponse
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer, EstudanteSerializerV2, MatriculaSerializer,ListaMatriculasEstudanteSerializer,ListaMatriculasCursoSerializer
from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .throttles import MatriculaAnonRateThrottle

# Create your views here.
# def estudantes(request):
#     if request.method == 'GET':
#         estudante = {
#             'id': 1,
#             'nome': 'Alex'
#         }
#         return JsonResponse(estudante)

class EstudanteViewSet(viewsets.ModelViewSet):

    """
    Descrição da ViewSet:
    - Endpoint para CRUD de estudantes.

    Campos de ordenação:
    - nome: permite ordenar os resultados por nome.

    Campos de pesquisa:
    - nome: permite pesquisar os resultados por nome.
    - cpf: permite pesquisar os resultados por CPF.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Classe de Serializer:
    - EstudanteSerializer: usado para serialização e desserialização de dados.
    - Se a versão da API for 'v2', usa EstudanteSerializerV2.
    """

    # Possibilita acesso às views somente se autenticado (Pode ser omitido se fizer o ajuste em settings.py->REST_FRAMEWORK->classes padrão de autenticação e permissão)
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated] # Acesso se estiver logado (sem restrição de tipo de usuário)
    #permission_classes = [IsAuthenticated, IsAdminUser] # Acesso se estiver logado e for usuário Admin (pode deixar apenas o IsAdminUser)
    # permission_classes = [IsAuthenticatedOrReadOnly] #Se estiver logado acessa completamente, mas se não estiver, somente acessa o get

    # Para garantir sucesso na paginação, deve-se ordernar a lista de alguma forma
    queryset = Estudante.objects.all().order_by('id') #.order_by('nome') 
    # serializer_class = EstudanteSerializer #pegará automaticamente por meio da classe abaixo (função padrão)

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # passar ordenação como parâmetro GET após endpoint (estudantes/?ordering=<parâmetro>)
    ordering_fields = ['nome', 'email', 'cpf', 'data_nascimento'] # acrescente o campo que poderá realizar ordenação
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de cursos.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """

    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de matrículas.

    Métodos HTTP Permitidos:
    - GET, POST

    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"] # limitando os métodos http permitidos para essa view

class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
     
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

# Docstring -> importante para documentação no Swagger
class ListaMatriculaCurso(generics.ListAPIView):

    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """

    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculasCursoSerializer