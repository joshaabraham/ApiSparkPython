from SparkApp.modelsBo import SparkUser
from SparkApp.serializers.SparkUser_srlz import SparkUserSerializer

from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



#@csrf_exempt
@api_view(['POST'])
def authentificationRegister(request):
    if request.method == 'POST':
        auth_data=JSONParser().parse(request)
        auth_serializer = SparkUserSerializer(data=auth_data, partial=True)

        #serializer = SparkUserSerializer(data=request.body, partial=True)
        #data = JSONParser().parse(serializer)
        data={}
        if auth_serializer.is_valid():
            sparkUser = auth_serializer.save()
            data['response'] = "Successfully registered a new user."
            data['email'] = sparkUser.email
            token = Token.objects.get(user=sparkUser).key
            data['token'] = token
        else:
            data = auth_serializer.errors
        return Response[data]


@api_view(['POST'])
def authentificationLogin(request,id=0):
     if request.method == 'POST':
      auth_data=JSONParser().parse(request)
      auth_serializer = SparkUserSerializer(data=auth_data)
      if auth_serializer.is_valid():
            auth_serializer.save()
            post_save.connect(authentificationLogin, sender=SparkUser)
            return JsonResponse("Registered Successfully!!" , safe=False)
      return JsonResponse("Failed to Register.",safe=False)



#@receiver(post_save, sender=SparkUser)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        token = Token.objects.create(user=instance)
#        print(token)

