
from rest_framework import serializers
from SparkApp.modelsBo.UserOrientedRelations import CentreInteret


class CentreInteretSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentreInteret
        fields = ('CentreInteretId')
