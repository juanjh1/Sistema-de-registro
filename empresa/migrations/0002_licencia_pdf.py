# Generated by Django 4.2 on 2023-05-23 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="licencia",
            name="pdf",
            field=models.FileField(default=1, upload_to="media/"),
            preserve_default=False,
        ),
    ]