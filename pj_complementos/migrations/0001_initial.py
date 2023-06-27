# Generated by Django 3.2.19 on 2023-06-26 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PJComplementos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('salario', models.FloatField()),
                ('faculdade', models.FloatField()),
                ('credito_convenio', models.FloatField()),
                ('auxilio_moradia', models.FloatField()),
                ('outros_creditos', models.FloatField()),
                ('adiantamento', models.FloatField()),
                ('desconto_convenio', models.FloatField()),
                ('outros_descontos', models.FloatField()),
                ('data_pagamento', models.DateField()),
                ('data_emissao', models.DateTimeField(default=django.utils.timezone.now)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PJComplemento',
                'verbose_name_plural': 'PJComplementos',
                'db_table': 'pj_complementos',
            },
        ),
    ]
