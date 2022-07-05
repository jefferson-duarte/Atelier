from django.shortcuts import render


def post_create(request):
    return render(request, 'post/create_post.html')


def lista_post(request):
    return render(request, 'post/lista_post.html')