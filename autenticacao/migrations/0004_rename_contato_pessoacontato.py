# Generated by Django 4.0.5 on 2022-06-06 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0003_remove_contato_foto_remove_contato_sobre_nome_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contato',
            new_name='PessoaContato',
        ),
    ]