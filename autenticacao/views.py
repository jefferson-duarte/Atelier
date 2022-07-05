from django.shortcuts import redirect, render
from django.http import HttpResponse


def login(request):
    if request.method == 'GET':
        return render(request, 'autenticacao/login.html')
    
    if request.method == 'POST':
        return redirect(request, 'post/lista_post.html')
    

def reset_senha(request):
    return render(request, 'autenticacao/reset.html')
