
from rest_framework import serializers
from SparkApp.modelsBo.UserOrientedRelations import GroupeDeCommunication


class GroupeDeCommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupeDeCommunication
        fields = ('GroupeDeCommunicationId')