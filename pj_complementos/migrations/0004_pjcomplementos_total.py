# Generated by Django 3.2.19 on 2023-06-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pj_complementos', '0003_pjcomplementos_ajuda_custo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pjcomplementos',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
