from rest_framework import serializers
from SparkApp.modelsBo.PublicationsTypes import Publicite




class PubliciteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicite
        fields = ('PubliciteId')