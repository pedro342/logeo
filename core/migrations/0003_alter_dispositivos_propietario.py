# Generated by Django 4.2.5 on 2023-10-11 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_dispositivos_propietario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivos',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dispositivos', to=settings.AUTH_USER_MODEL),
        ),
    ]
