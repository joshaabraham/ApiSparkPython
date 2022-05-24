
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from SparkApp.modelsBo import Profil
from SparkApp.serializers.profil_srlz import ProfilSerializer




@csrf_exempt
def saveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)
