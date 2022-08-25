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

        techs = validated_data.pop("techs")

        project = BackEnd.objects.create(**validated_data)

        for tech in techs:
            project.techs.add(Technology.objects.get_or_create(name=tech["name"])[0])

        return project


class DeleteTechSerializer(serializers.ModelSerializer):
    techs = TechSerializer(many=True)

    class Meta:
        model = BackEnd
        fields = ["id", "title", "description", "code_url", "techs"]
        read_only_fields = ["title", "description", "code_url"]

    def update(self, instance, validated_data):

        for tech in validated_data["techs"]:
            instance.techs.remove(Technology.objects.get(name=tech["name"]))

        return instance


class AddTechSerializer(serializers.ModelSerializer):
    techs = TechSerializer(many=True)

    class Meta:
        model = BackEnd
        fields = ["id", "title", "description", "code_url", "techs"]
        read_only_fields = ["title", "description", "code_url"]

    def update(self, instance, validated_data):

        for tech in validated_data["techs"]:
            instance.techs.add(Technology.objects.get(name=tech["name"]))

        return instance
