# from django.shortcuts import render
from django.http import JsonResponse
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer, MatriculaSerializer,ListaMatriculasEstudanteSerializer,ListaMatriculasCursoSerializer
from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
# def estudantes(request):
#     if request.method == 'GET':
#         estudante = {
#             'id': 1,
#             'nome': 'Alex'
#         }
#         return JsonResponse(estudante)

class EstudanteViewSet(viewsets.ModelViewSet):
    # Possibilita acesso às views somente se autenticado (Pode ser omitido se fizer o ajuste em settings.py->REST_FRAMEWORK->classes padrão de autenticação e permissão)
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated] # Acesso se estiver logado (sem restrição de tipo de usuário)
    #permission_classes = [IsAuthenticated, IsAdminUser] # Acesso se estiver logado e for usuário Admin (pode deixar apenas o IsAdminUser)
    # permission_classes = [IsAuthenticatedOrReadOnly] #Se estiver logado acessa completamente, mas se não estiver, somente acessa o get

    # Para garantir sucesso na paginação, deve-se ordernar a lista de alguma forma
    queryset = Estudante.objects.all() #.order_by('nome') 
    serializer_class = EstudanteSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome', 'email']


class CursoViewSet(viewsets.ModelViewSet):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudante(generics.ListAPIView):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer