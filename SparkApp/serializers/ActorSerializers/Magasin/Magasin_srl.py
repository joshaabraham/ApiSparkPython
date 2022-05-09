from SparkApp.modelsBo.ActorModels import Magasin
import uuid
from rest_framework import serializers


class MagasinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magasin
        fields = ('MagasinId')