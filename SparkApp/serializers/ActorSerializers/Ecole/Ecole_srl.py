from SparkApp.modelsBo.ActorModels import Ecole
import uuid
from rest_framework import serializers


class EcoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecole
        fields = ('EcoleId')