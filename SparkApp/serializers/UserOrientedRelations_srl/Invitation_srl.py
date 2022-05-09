
from rest_framework import serializers
from SparkApp.modelsBo.UserOrientedRelations import InvitationClass


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationClass
        fields = ('InvitationId')