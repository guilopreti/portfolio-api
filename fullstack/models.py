import uuid

from django.db import models
from django.utils import timezone


# Create your models here.
class FullStack(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=False)

    registration_date = models.DateTimeField(default=timezone.now)

    front_description = models.TextField(max_length=1000, null=False)
    back_description = models.TextField(max_length=1000, null=False)

    img_url = models.CharField(max_length=255, null=False)
    preview_url = models.CharField(max_length=255, null=False)

    front_code_url = models.CharField(max_length=255, null=False)
    back_code_url = models.CharField(max_length=255, null=False)

    front_techs = models.ManyToManyField(
        "techs.Technology", related_name="full_front_projects"
    )
    back_techs = models.ManyToManyField(
        "techs.Technology", related_name="full_back_projects"
    )
    both_techs = models.ManyToManyField(
        "techs.Technology", related_name="full_both_projects"
    )
