from rest_framework import serializers
from SparkApp.modelsBo.ActorModels import AuteurClass



class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuteurClass
        fields = ('AuteurId')

