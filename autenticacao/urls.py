from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('reset/', views.reset_senha, name='reset'),
    path('logout/', views.logout, name='logout'),
]
