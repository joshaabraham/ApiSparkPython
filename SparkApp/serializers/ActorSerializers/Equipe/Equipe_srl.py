from SparkApp.modelsBo.ActorModels import Equipe
import uuid
from rest_framework import serializers


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = ('EquipeId')