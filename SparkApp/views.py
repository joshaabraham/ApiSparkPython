from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .modelsBo import Authentification, Profil
from SparkApp.serializers import AuthentificationSerializer,ProfilSerializer

from django.core.files.storage import default_storage

from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response


from django.contrib.auth.models import User


from SparkApp.Controllers import configurationApi, profilApi, authentificationApi

# Create your views here.

#@csrf_exempt
#def authentificationApi(request,id=0):
#    if request.method=='GET':
#        authentifications = Authentification.objects.all()
#        authentifications_serializer = AuthentificationSerializer(authentifications, many=True)
#        return JsonResponse(authentifications_serializer.data, safe=False)

#    elif request.method=='POST':
#        authentifications_data=JSONParser().parse(request)
#        authentification_serializer = AuthentificationSerializer(data=authentifications_data)
#        if authentification_serializer.is_valid():
#            authentification_serializer.save()
#            return JsonResponse("Added Successfully!!" , safe=False)
#        return JsonResponse("Failed to Add.",safe=False)
    
#    elif request.method=='PUT':
#        authentification_data = JSONParser().parse(request)
#        authentification=Authentification.objects.get(UserId=authentification_data['UserId'])
#        authentification_serializer=AuthentificationSerializer(authentification,data=authentification_data)
#        if authentification_serializer.is_valid():
#            authentification_serializer.save()
#            return JsonResponse("Updated Successfully!!", safe=False)
#        return JsonResponse("Failed to Update.", safe=False)

#    elif request.method=='DELETE':
#        authentification=Authentification.objects.get(UserId=id)
#        authentification.delete()
#        return JsonResponse("Deleted Succeffully!!", safe=False)

#@csrf_exempt
#def profilApi(request,id=0):
#    if request.method=='GET':
#        profils = Profil.objects.all()
#        profils_serializer = ProfilSerializer(profils, many=True)
#        return JsonResponse(profils_serializer.data, safe=False)

#    elif request.method=='POST':
#        profil_data=JSONParser().parse(request)
#        profil_serializer = ProfilSerializer(data=profil_data)
#        if profil_serializer.is_valid():
#            profil_serializer.save()
#            return JsonResponse("Added Successfully!!" , safe=False)
#        return JsonResponse("Failed to Add.",safe=False)
    
#    elif request.method=='PUT':
#        profil_data = JSONParser().parse(request)
#        profil=Profil.objects.get(ProfilId=profil_data['ProfilId'])
#        profil_serializer=ProfilSerializer(profil,data=profil_data)
#        if profil_serializer.is_valid():
#            profil_serializer.save()
#            return JsonResponse("Updated Successfully!!", safe=False)
#        return JsonResponse("Failed to Update.", safe=False)

#    elif request.method=='DELETE':
#         profil=Profil.objects.get(ProfilId=id)
#         profil.delete()
#         return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)



#@csrf_exempt
#def getAuthenticated(request):
#    if request.method=='GET':
#        permission_classes = (IsAuthenticated,)           
#        content = {'message': 'IsAuthenticated !'}
#        return JsonResponse(content)
