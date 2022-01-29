from spoiled.models import Spoiled, Nomenclature
from rest_framework import serializers

class SpoiledSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spoiled
        exclude = ["picture", "content_type"]
        read_only = ["created_at", "updated_at"]