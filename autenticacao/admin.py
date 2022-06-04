from django.contrib import admin
from .models import Contato
    

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobre_nome', 'email', 'telefone')
    list_editable = ('telefone', 'email')
    list_per_page = 5
    list_display_links = ('nome', 'sobre_nome')
    list_filter = ('nome',)

admin.site.register(Contato, ContatoAdmin)