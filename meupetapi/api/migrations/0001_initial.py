# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-29 00:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passeador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('primeiroNome', models.CharField(max_length=255)),
                ('segundoNome', models.CharField(max_length=255)),
                ('idade', models.DateField()),
                ('regiao', models.CharField(max_length=100)),
                ('estaPasseando', models.BooleanField()),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Passeio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('duracao', models.DurationField()),
                ('descricaoPasseio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('raca', models.CharField(max_length=255)),
                ('tamanho', models.CharField(choices=[(b'P', b'Pequeno'), (b'M', b'Medio'), (b'G', b'Grande')], max_length=1)),
                ('descricaoPet', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('primeiroNome', models.CharField(max_length=255)),
                ('segundoNome', models.CharField(max_length=255)),
                ('idade', models.DateField()),
                ('email', models.EmailField(max_length=255)),
                ('senha', models.CharField(max_length=30)),
                ('descricaoUsuario', models.TextField()),
                ('regiao', models.CharField(default=b'', max_length=100)),
                ('estaPasseando', models.BooleanField(default=False)),
                ('tipousuario', models.ManyToManyField(to='api.TipoUsuario')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='dono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Usuario'),
        ),
    ]
