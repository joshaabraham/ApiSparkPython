from rest_framework import serializers
from SparkApp.modelsBo.PublicationsTypes import MediaVideo




class MediaVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaVideo
        fields = ('MediaVideoId')