from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('create/', views.post_create, name='create'),
    path('reset/', views.reset_senha, name='reset'),
]
