# Generated by Django 4.2.6 on 2023-11-07 23:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_remove_certificate_topics_certificate_topics"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="youtube_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="certificate",
            name="image",
            field=models.ImageField(upload_to="media/certificates"),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="media/projects"),
        ),
    ]
