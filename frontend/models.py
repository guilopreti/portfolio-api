import uuid

from django.db import models
from django.utils import timezone


# Create your models here.
class FrontEnd(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=1000, null=False)
    img_url = models.CharField(max_length=255, null=False)
    preview_url = models.CharField(max_length=255, null=False)
    code_url = models.CharField(max_length=255, null=False)
    registration_date = models.DateTimeField(default=timezone.now)
    techs = models.ManyToManyField("techs.Technology", related_name="front_projects")
