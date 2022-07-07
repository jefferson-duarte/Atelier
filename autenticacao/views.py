from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            messages.add_message(request, constants.ERROR, 'Você já está logado.')
            return redirect('/')
        return render(request, 'autenticacao/login.html')
    
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('password')
        
        
        user = auth.authenticate(
            username = usuario,
            password=senha,
        )
        
        if not user:
            messages.add_message(request, constants.ERROR, 'Usuário não cadastrado.')
            return redirect('/auth/login')
        else:
            auth.login(request, user)
            return redirect('/create')
    
    
def logout(request):
    auth.logout(request)
    messages.add_message(request, constants.SUCCESS, 'Logout realizado com sucesso.')
    return redirect('/auth/login')
    
    
def reset_senha(request):
    return render(request, 'autenticacao/reset.html')
