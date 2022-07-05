from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
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
            return redirect('/auth/login')
        else:
            auth.login(request, user)
            return redirect('/create')
    
    
def logout(request):
    auth.logout(request)
    return redirect('/auth/login')
    
    
def reset_senha(request):
    return render(request, 'autenticacao/reset.html')
