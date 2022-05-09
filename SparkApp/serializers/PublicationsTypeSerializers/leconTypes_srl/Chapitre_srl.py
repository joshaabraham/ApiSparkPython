from rest_framework import serializers
from SparkApp.modelsBo.PublicationsTypes.leconTypes import Chapitre




class ChapitreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapitre
        fields = ('ChapitreId')
