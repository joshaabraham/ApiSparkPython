from SparkApp.modelsBo.ActorModels import Club
import uuid
from rest_framework import serializers


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('ClubId')
