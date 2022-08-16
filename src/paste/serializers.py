from rest_framework import serializers
from .models import Paste

class PasteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paste