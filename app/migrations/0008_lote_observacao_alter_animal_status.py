# Generated by Django 5.0.7 on 2024-08-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_procedimentomanejo_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='observacao',
            field=models.TextField(blank=True, null=True, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
    ]
