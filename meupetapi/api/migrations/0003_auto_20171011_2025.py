# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 23:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171011_2019'),
    ]

    operations = [
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
                ('tipousuario', models.ManyToManyField(to='api.TipoUsuario')),
            ],
        ),
        migrations.RemoveField(
            model_name='dono',
            name='tipousuario',
        ),
        migrations.RemoveField(
            model_name='passeador',
            name='descricaoUsuario',
        ),
        migrations.RemoveField(
            model_name='passeador',
            name='senha',
        ),
        migrations.RemoveField(
            model_name='passeador',
            name='tipousuario',
        ),
        migrations.AlterField(
            model_name='pet',
            name='dono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Usuario'),
        ),
        migrations.DeleteModel(
            name='Dono',
        ),
    ]
