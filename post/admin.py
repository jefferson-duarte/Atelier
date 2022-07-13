from django.contrib import admin
from .models import CreatePost


class CreatePostAdmin(admin.ModelAdmin):
    list_display = [
        'titulo', 'descricao_curta',
    ]
    
    list_editable = [
        'descricao_curta',
    ]
    
    
admin.site.register(CreatePost, CreatePostAdmin)
