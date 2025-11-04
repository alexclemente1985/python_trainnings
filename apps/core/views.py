from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario
# Create your views here.

@login_required #decorator que obriga o login para acesso à view -> redireciona para tela de login (registration)
def home(request):
    data = {}
    data['usuario'] = request.user

    return render(request, 'core/index.html', data)