from SparkApp.modelsBo.ActorModels import Reseau
import uuid
from rest_framework import serializers


class ReseauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reseau
        fields = ('ReseauId')