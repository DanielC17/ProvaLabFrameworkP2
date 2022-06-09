from django.shortcuts import render
from postagem.models import Postagem

# Create your views here.


def index(request):

    postagens = Postagem.objects.all()

    return render(request, 'postagem/index.html', {'postagens':postagens})


def add(request):
    if request.method == "POST":
        postagem = Postagem()
        postagem.nome_estagiario = 
        postagem.postagem
