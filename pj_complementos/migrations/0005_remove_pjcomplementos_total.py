# Generated by Django 3.2.19 on 2023-06-27 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pj_complementos', '0004_pjcomplementos_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pjcomplementos',
            name='total',
        ),
    ]