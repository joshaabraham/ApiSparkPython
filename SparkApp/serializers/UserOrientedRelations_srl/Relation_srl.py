
from rest_framework import serializers
from SparkApp.modelsBo.UserOrientedRelations import Relation


class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = ('RelationId')
