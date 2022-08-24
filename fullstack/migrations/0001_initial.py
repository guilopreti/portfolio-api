# Generated by Django 4.1 on 2022-08-24 04:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("techs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FullStack",
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
                ("front_description", models.TextField(max_length=1000)),
                ("back_description", models.TextField(max_length=1000)),
                ("img_url", models.CharField(max_length=255)),
                ("preview_url", models.CharField(max_length=255)),
                ("front_code_url", models.CharField(max_length=255)),
                ("back_code_url", models.CharField(max_length=255)),
                (
                    "back_techs",
                    models.ManyToManyField(
                        related_name="full_back_projects", to="techs.technology"
                    ),
                ),
                (
                    "both_techs",
                    models.ManyToManyField(
                        related_name="full_both_projects", to="techs.technology"
                    ),
                ),
                (
                    "front_techs",
                    models.ManyToManyField(
                        related_name="full_front_projects", to="techs.technology"
                    ),
                ),
            ],
        ),
    ]
