# Generated by Django 3.2.19 on 2023-06-09 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacoes_entradas', '0003_alter_solicitacoesentradas_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacoesentradas',
            name='data_criacao',
            field=models.DateField(default=datetime.date(2023, 6, 9)),
        ),
    ]