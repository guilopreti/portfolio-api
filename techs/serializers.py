from rest_framework import serializers

from .models import Technology


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["id", "name"]
