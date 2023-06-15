# Generated by Django 3.2.19 on 2023-06-12 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paletes_controles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paletescontroles',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='paletescontroles',
            name='localizacao_atual',
            field=models.CharField(default='MOV', max_length=3),
        ),
        migrations.AlterField(
            model_name='paletescontroles',
            name='tipo_palete',
            field=models.CharField(choices=[('PBR', 'Pbr'), ('CHEP', 'Chep')], max_length=4),
        ),
    ]