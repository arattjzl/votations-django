# Generated by Django 5.0.1 on 2024-04-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacion', '0002_votacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
    ]