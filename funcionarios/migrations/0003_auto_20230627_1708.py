# Generated by Django 3.2.19 on 2023-06-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_rename_ag_funcionarios_agencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionarios',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='pix',
            field=models.CharField(max_length=30),
        ),
    ]
