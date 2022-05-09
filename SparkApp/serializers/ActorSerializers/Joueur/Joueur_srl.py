from SparkApp.modelsBo.ActorModels import Joueur
import uuid
from rest_framework import serializers


class JoueurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joueur
        fields = ('JoueurId')