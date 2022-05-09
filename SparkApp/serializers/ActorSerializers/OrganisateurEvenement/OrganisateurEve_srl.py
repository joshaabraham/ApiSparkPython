from rest_framework import serializers
from SparkApp.modelsBo.ActorModels import *



class OrganisateurEveSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganisateurEvenement
        fields = ('OrganisateurEveId')