# Generated by Django 4.2.7 on 2023-11-10 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pecuaria', '0002_lote_loteanimal_parto_rename_especieanimal_especie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='manejo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='parto',
            name='created_at',
        ),
    ]