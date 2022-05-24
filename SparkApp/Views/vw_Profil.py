from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from SparkApp.modelsBo import Profil
from SparkApp.serializers.profil_srlz import ProfilSerializer



@csrf_exempt
def profilApi(request,id=0):
    if request.method=='GET':
        profils = Profil.objects.all()
        profils_serializer = ProfilSerializer(profils, many=True)
        return JsonResponse(profils_serializer.data, safe=False)

    elif request.method=='POST':
        profil_data=JSONParser().parse(request)
        profil_serializer = ProfilSerializer(data=profil_data)
        if profil_serializer.is_valid():
            profil_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        profil_data = JSONParser().parse(request)
        profil=Profil.objects.get(ProfilId=profil_data['ProfilId'])
        profil_serializer=ProfilSerializer(profil,data=profil_data)
        if profil_serializer.is_valid():
            profil_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
         profil=Profil.objects.get(ProfilId=id)
         profil.delete()
         return JsonResponse("Deleted Succeffully!!", safe=False)