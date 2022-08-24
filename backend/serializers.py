from rest_framework import serializers
from techs.models import Technology

from .models import BackEnd


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["name"]


class BackendSerializer(serializers.ModelSerializer):
    techs = TechSerializer(many=True)

    class Meta:
        model = BackEnd
        fields = ["id", "title", "description", "code_url", "techs"]

    def create(self, validated_data):

        techs = []
        for tech in validated_data["techs"]:
            techs.append(Technology.objects.get_or_create(name=tech["name"])[0])

        del validated_data["techs"]

        project = BackEnd.objects.create(**validated_data)

        project.techs.set(techs)

        return project
