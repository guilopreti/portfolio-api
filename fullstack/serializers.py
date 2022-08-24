from rest_framework import serializers
from techs.models import Technology

from .models import FullStack


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["name"]


class FullstackSerializer(serializers.ModelSerializer):
    front_techs = TechSerializer(many=True)
    back_techs = TechSerializer(many=True)
    both_techs = TechSerializer(many=True, required=False)

    class Meta:
        model = FullStack
        fields = [
            "id",
            "title",
            "front_description",
            "back_description",
            "img_url",
            "preview_url",
            "front_code_url",
            "back_code_url",
            "front_techs",
            "back_techs",
            "both_techs",
        ]

    def create(self, validated_data):

        front_techs = validated_data.pop("front_techs")
        back_techs = validated_data.pop("back_techs")

        if "both_techs" in validated_data.keys():
            both_techs = validated_data.pop("both_techs")

            project = FullStack.objects.create(**validated_data)

            for both in both_techs:
                project.both_techs.add(
                    Technology.objects.get_or_create(name=both["name"])[0]
                )
        else:
            project = FullStack.objects.create(**validated_data)

        for front in front_techs:
            project.front_techs.add(
                Technology.objects.get_or_create(name=front["name"])[0]
            )

        for back in back_techs:
            project.back_techs.add(
                Technology.objects.get_or_create(name=back["name"])[0]
            )

        return project
