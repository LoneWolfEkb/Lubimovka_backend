from rest_framework import serializers

from apps.info.models import Festival


class FestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festival
        exclude = ("created", "modified")
        depth = 1


class YearsSerializer(serializers.Serializer):
    years = serializers.ListField(child=serializers.IntegerField())