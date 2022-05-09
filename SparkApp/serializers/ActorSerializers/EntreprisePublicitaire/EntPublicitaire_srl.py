from SparkApp.modelsBo.ActorModels import EntreprisePublicitaire
import uuid
from rest_framework import serializers


class EntreprisePublicitaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntreprisePublicitaire
        fields = ('EPPId')