from django.shortcuts import render
from django.http import HttpResponse


def cadastro(request):
    return HttpResponse('Cadastro')


def login(request):
    return HttpResponse('Login')


def logout(request):
    return HttpResponse('Logout')
