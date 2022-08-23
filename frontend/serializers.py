from rest_framework import serializers
from techs.models import Technology

from .models import FrontEnd


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["name"]


class FrontendSerializer(serializers.ModelSerializer):
    techs = TechSerializer(many=True)

    class Meta:
        model = FrontEnd
        fields = [
            "id",
            "title",
            "description",
            "img_url",
            "preview_url",
            "code_url",
            "techs",
        ]

    def create(self, validated_data):

        techs = []
        for tech in validated_data["techs"]:
            techs.append(Technology.objects.get_or_create(name=tech["name"])[0])

        del validated_data["techs"]

        project = FrontEnd.objects.create(**validated_data)

        project.techs.set(techs)

        return project
