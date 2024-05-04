# Generated by Django 5.0.1 on 2024-04-19 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido_pat', models.CharField(max_length=250)),
                ('apellido_mat', models.CharField(max_length=250)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='fotos', verbose_name='Imagen')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votacion.partido', verbose_name='Partido')),
            ],
        ),
    ]