from rest_framework import serializers
from SparkApp.modelsBo.PublicationsTypes import AlbumPhoto




class AlbumPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPhoto
        fields = ('AlbumPhotoId')
