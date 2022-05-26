
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from SparkApp.modelsBo import Authentification
from SparkApp.serializers.authentication_srl import  AuthentificationSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated




from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token




@csrf_exempt
def authentificationApi(request,id=0):
    if request.method=='GET':
        authentications = Authentification.objects.all()
        auth_serializer = AuthentificationSerializer(authentications, many=True)
        return JsonResponse(auth_serializer.data, safe=False)

    elif request.method=='POST':
        auth_data=JSONParser().parse(request)
        auth_serializer = AuthentificationSerializer(data=auth_data)
        if auth_serializer.is_valid():
            auth_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        auth_data = JSONParser().parse(request)
        authentication=Authentification.objects.get(AuthentificationId=auth_data['userId'])
        auth_serializer=AuthentificationSerializer(authentication,data=auth_data)
        if auth_serializer.is_valid():
            auth_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
         authentication=Authentification.objects.get(AuthentificationId=id)
         authentication.delete()
         return JsonResponse("Deleted Succeffully!!", safe=False)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

