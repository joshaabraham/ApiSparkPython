from rest_framework import serializers
from SparkApp.modelsBo.PublicationsTypes import Publications




class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = ('PublicationsId')