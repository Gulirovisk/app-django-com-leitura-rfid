# Generated by Django 5.0.7 on 2024-08-08 13:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_parto_femea_content_type_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BovinoCorte',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.animal')),
                ('modo_de_criacao', models.CharField(blank=True, choices=[('Confinamento', 'Confinamento'), ('Pasto', 'Pasto')], max_length=255, null=True, verbose_name='Modo de criação')),
                ('local', models.CharField(blank=True, choices=[], max_length=255, null=True, verbose_name='Local')),
            ],
            options={
                'verbose_name': 'Bovino de Corte',
                'verbose_name_plural': 'Bovinos de Corte',
                'ordering': ['identificacao_unica'],
            },
            bases=('app.animal',),
        ),
        migrations.CreateModel(
            name='BovinoLeite',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.animal')),
                ('nome', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome')),
                ('grau_sangue', models.CharField(blank=True, max_length=255, null=True, verbose_name='Grau de sangue')),
                ('pelagem', models.CharField(blank=True, max_length=255, null=True, verbose_name='Pelagem')),
            ],
            options={
                'verbose_name': 'Bovino de Leite',
                'verbose_name_plural': 'Bovinos de Leite',
                'ordering': ['identificacao_unica'],
            },
            bases=('app.animal',),
        ),
        migrations.CreateModel(
            name='Procedimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Procedimento',
                'verbose_name_plural': 'Procedimentos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('fabricante', models.CharField(blank=True, max_length=255, null=True, verbose_name='Fabricante')),
                ('quantidade', models.PositiveIntegerField(default=0, verbose_name='Quantidade')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='TipoProcedimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Tipo do Procedimento',
                'verbose_name_plural': 'Tipos de Procedimento',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='TipoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Tipo do Produto',
                'verbose_name_plural': 'Tipos de Produto',
                'ordering': ['nome'],
            },
        ),
        migrations.AlterField(
            model_name='baia',
            name='sala',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='baia_sala', to='app.sala', verbose_name='Sala'),
        ),
        migrations.AlterField(
            model_name='galpao',
            name='setor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='galpao_setor', to='app.setor', verbose_name='Setor'),
        ),
        migrations.AlterField(
            model_name='parto',
            name='femea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parto_femea', to='app.animal', verbose_name='Fêmea'),
        ),
        migrations.AlterField(
            model_name='parto',
            name='macho',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parto_macho', to='app.animal', verbose_name='Macho'),
        ),
        migrations.AlterField(
            model_name='sala',
            name='galpao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sala_galpao', to='app.galpao', verbose_name='Galpão'),
        ),
        migrations.AlterField(
            model_name='setor',
            name='usuarios',
            field=models.ManyToManyField(blank=True, related_name='setor_usuarios', to=settings.AUTH_USER_MODEL, verbose_name='Usuários do setor'),
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('setor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='funcionario_setor', to='app.setor', verbose_name='Setor')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(verbose_name='Número')),
                ('animais', models.ManyToManyField(blank=True, related_name='lote_animais', to='app.animal', verbose_name='Animais')),
                ('baia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lote_baia', to='app.baia', verbose_name='Baia')),
                ('setor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lote_setor', to='app.setor', verbose_name='Setor')),
            ],
            options={
                'verbose_name': 'Lote',
                'verbose_name_plural': 'Lotes',
                'ordering': ['numero'],
            },
        ),
        migrations.CreateModel(
            name='Manejo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_do_manejo', models.DateTimeField(verbose_name='Data e hora do manejo')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('animal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manejo_animal', to='app.animal', verbose_name='Animal')),
                ('funcionario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manejo_funcionario', to='app.funcionario', verbose_name='Funcionário')),
                ('setor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manejo_setor', to='app.setor', verbose_name='Setor')),
            ],
            options={
                'verbose_name': 'Manejo',
                'verbose_name_plural': 'Manejos',
                'ordering': ['data_hora_do_manejo'],
            },
        ),
        migrations.CreateModel(
            name='ProcedimentoManejo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Valor')),
                ('manejo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='procedimento_manejo', to='app.manejo', verbose_name='Manejo')),
                ('procedimento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='procedimento_procedimento', to='app.procedimento', verbose_name='Procedimento')),
            ],
            options={
                'verbose_name': 'Procedimento do Manejo',
                'verbose_name_plural': 'Procedimentos do Manejo',
                'ordering': ['manejo'],
            },
        ),
        migrations.CreateModel(
            name='ProdutoManejo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=0, verbose_name='Quantidade')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Valor')),
                ('manejo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produto_manejo', to='app.manejo', verbose_name='Manejo')),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produto_produto', to='app.produto', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Produto do Manejo',
                'verbose_name_plural': 'Produtos do Manejo',
                'ordering': ['manejo'],
            },
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_da_saida', models.DateTimeField(verbose_name='Data e hora da saída')),
                ('tipo', models.CharField(choices=[('Morte natural', 'Morte natural'), ('Abate sanitário', 'Abate sanitário'), ('Descarte', 'Descarte'), ('Outros', 'Outros')], max_length=255, verbose_name='Tipo de saída')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('animais', models.ManyToManyField(blank=True, related_name='saida_animais', to='app.animal', verbose_name='Animais')),
                ('setor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='saida_setor', to='app.setor', verbose_name='Setor')),
            ],
            options={
                'verbose_name': 'Saída',
                'verbose_name_plural': 'Saídas',
                'ordering': ['data_hora_da_saida'],
            },
        ),
        migrations.AddField(
            model_name='procedimento',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='procedimento_tipo', to='app.tipoprocedimento', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.tipoproduto', verbose_name='Tipo'),
        ),
    ]