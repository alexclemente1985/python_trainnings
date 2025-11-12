from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from apps.core.serializers import GroupSerializer, UserSerializer
from apps.funcionarios.models import Funcionario
from rest_framework import viewsets
# Create your views here.

@login_required #decorator que obriga o login para acesso à view -> redireciona para tela de login (registration)
def home(request):
    data = {}
    data['usuario'] = request.user

    return render(request, 'core/index.html', data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer