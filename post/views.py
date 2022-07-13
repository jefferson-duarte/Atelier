from django.shortcuts import render
from .models import CreatePost


def post_create(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao_curta = request.POST.get('descricao_curta')
        descricao_longa = request.POST.get('descricao_longa')    
        
        novo_post = CreatePost(
            titulo=titulo,
            descricao_curta=descricao_curta,
            descricao_longa=descricao_longa,
        )
        
        novo_post.save()
    
    return render(request, 'post/create_post.html')


def lista_post(request):
    return render(request, 'post/lista_post.html')