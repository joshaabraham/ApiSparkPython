from rest_framework import serializers
from SparkApp.modelsBo import Authentification
#from django.contrib.auth.models import User, Group



class AuthentificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authentification
        fields = ('userId',
                    'name',
                    'email',
                    'motdepasse')
