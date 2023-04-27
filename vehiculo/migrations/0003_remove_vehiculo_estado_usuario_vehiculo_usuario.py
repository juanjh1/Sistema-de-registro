# Generated by Django 4.2 on 2023-04-26 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("vehiculo", "0002_vehiculo_estado_usuario"),
    ]

    operations = [
        migrations.RemoveField(model_name="vehiculo_estado", name="usuario",),
        migrations.AddField(
            model_name="vehiculo",
            name="usuario",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
