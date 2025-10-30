from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from galeria.models import Fotografia

# Create your views here.

def index(request):

    # fotografias = Fotografia.objects.all()
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) # para inverter a ordem -> "-data_fotografia"

    return render(request, 'galeria/index.html', {"cards":fotografias})

def imagem(request, foto_id):
        fotografia = get_object_or_404(Fotografia, pk=foto_id)
        return render(request, 'galeria/imagem.html', {"fotografia":fotografia})

def buscar(request):
      return render (request, 'galeria/buscar.html')