# Generated by Django 3.2.19 on 2023-07-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0006_auto_20230703_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionarios',
            name='genero',
            field=models.CharField(choices=[('HOMEM CISGÊNERO', 'Homem Cisgenero'), ('HOMEM TRANSGÊNERO', 'Homem Transgenero'), ('MULHER CISGÊNERO', 'Mulher Cisgenero'), ('MULHER TRANSGÊNERO', 'Mulher Transgenero'), ('NÃO BINÁRIO', 'Nao Binario'), ('NÃO QUERO INFORMAR', 'Nao Quero Informar')], max_length=25, null=True),
        ),
    ]
