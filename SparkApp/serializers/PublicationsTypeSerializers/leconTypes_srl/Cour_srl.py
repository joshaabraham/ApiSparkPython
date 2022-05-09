from rest_framework import serializers
from SparkApp.modelsBo.PublicationsTypes.leconTypes import Cour




class CourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cour
        fields = ('CourId')
