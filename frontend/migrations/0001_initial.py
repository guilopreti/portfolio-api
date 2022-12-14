# Generated by Django 4.1 on 2022-08-23 06:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("techs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FrontEnd",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=1000)),
                ("img_url", models.CharField(max_length=255)),
                ("preview_url", models.CharField(max_length=255)),
                ("code_url", models.CharField(max_length=255)),
                (
                    "techs",
                    models.ManyToManyField(
                        related_name="front_projects", to="techs.technology"
                    ),
                ),
            ],
        ),
    ]
