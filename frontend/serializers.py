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

        techs = validated_data.pop("techs")

        project = FrontEnd.objects.create(**validated_data)

        for tech in techs:
            project.techs.add(Technology.objects.get_or_create(name=tech["name"])[0])

        return project


class DeleteTechSerializer(serializers.ModelSerializer):
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
        read_only_fields = [
            "title",
            "description",
            "img_url",
            "preview_url",
            "code_url",
        ]

    def update(self, instance, validated_data):

        for tech in validated_data["techs"]:
            instance.techs.remove(Technology.objects.get(name=tech["name"]))

        return instance


class AddTechSerializer(serializers.ModelSerializer):
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
        read_only_fields = [
            "title",
            "description",
            "img_url",
            "preview_url",
            "code_url",
        ]

    def update(self, instance, validated_data):

        for tech in validated_data["techs"]:
            instance.techs.add(Technology.objects.get(name=tech["name"]))

        return instance
