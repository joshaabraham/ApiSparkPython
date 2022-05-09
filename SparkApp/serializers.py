from rest_framework import serializers
from SparkApp.modelsBo import Authentification, Profil
from django.contrib.auth.models import User, Group
from .serializers import *



class AuthentificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authentification
        fields = ('userId',
                  'name',
                  'motdepasse',
                  'email',
                  'username')

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ('ProfilId',
                  'ProfilName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
