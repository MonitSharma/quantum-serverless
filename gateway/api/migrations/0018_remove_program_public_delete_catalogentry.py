# Generated by Django 4.2.11 on 2024-04-08 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0017_alter_program_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="program",
            name="public",
        ),
        migrations.DeleteModel(
            name="CatalogEntry",
        ),
    ]
