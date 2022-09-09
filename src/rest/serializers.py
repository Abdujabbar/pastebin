from rest_framework import serializers
from app.models import Paste


class PasteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paste
        fields = ["name", "content", "short_url"]
