
from rest_framework import serializers
from SparkApp.modelsBo import SparkUser
#from django.contrib.auth.models import User, Group



class SparkUserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input-type':'password'}, write_only=True)

    class Meta:
        model = SparkUser
        fields = ['username', 'email', 'password', 'password2']
        extra_kwars ={ 
            'password':{'write_only': True}
        }

    def save(self):
        sparkUser = SparkUser(
                        email=self.validated_data['email'],
                        username=self.validated_data['username']
            )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        sparkUser.set_password(password)
        sparkUser.save()
        return sparkUser