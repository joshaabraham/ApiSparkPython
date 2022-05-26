
from rest_framework import serializers
from SparkApp.modelsBo import SparkUser


class SparkUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SparkUser
    
        #last_login = serializers.DateTimeField()
        #is_superuser = serializers.BooleanField(default=False) 
        #username = serializers.CharField()
        #first_name = serializers.CharField()
        #last_name = serializers.CharField()
        #email  = serializers.EmailField() 
        #is_staff  = serializers.BooleanField(default=False)
        #is_active = serializers.BooleanField(default=True) 
        #date_joined = serializers.DateTimeField()
        #sparkuserID = serializers.CharField()
        password2  =  serializers.CharField()


        fields = [ 'email', 'username', 'password']
        extra_kwars ={ 
            'password':{'write_only': True}
        }

    def save(self):
        sparkUser = SparkUser(
                        email=self.validated_data['email'],
                        username=self.validated_data['username'],
                        password=self.validated_data['password']
            )
       
        #password2=self.validated_data['password2']

        #if password != password2:
        #    raise serializers.ValidationError({'password': 'Passwords must match.'})
        sparkUser.set_password(sparkUser.password)
        sparkUser.save()
        return sparkUser