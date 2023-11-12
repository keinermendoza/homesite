# Generated by Django 4.2.6 on 2023-11-08 00:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_rename_certificatetopic_tecnology_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="topics",
            field=models.ManyToManyField(
                related_name="certificates", to="blog.tecnology"
            ),
        ),
    ]