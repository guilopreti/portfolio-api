import uuid

from django.db import models


# Create your models here.
class BackEnd(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=1000, null=False)
    code_url = models.CharField(max_length=255, null=False)
    techs = models.ManyToManyField("techs.Technology", related_name="back_projects")
