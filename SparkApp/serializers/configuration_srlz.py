from rest_framework import serializers
from SparkApp.modelsBo import *
from django.contrib.auth.models import User, Group

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ('ConfigurationID')

