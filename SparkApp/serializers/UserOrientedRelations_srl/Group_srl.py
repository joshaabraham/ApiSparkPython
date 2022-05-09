
from rest_framework import serializers
from SparkApp.modelsBo.UserOrientedRelations import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('GroupId')