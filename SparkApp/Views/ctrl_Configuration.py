from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from SparkApp.modelsBo import Configuration
from SparkApp.serializers.configuration_srlz import ConfigurationSerializer



@csrf_exempt
def configurationApi(request,id=0):
    if request.method=='GET':
        configurations = Configuration.objects.all()
        configurations_serializer = ConfigurationSerializer(configurations, many=True)
        return JsonResponse(configurations_serializer.data, safe=False)

    elif request.method=='POST':
        configuration_data=JSONParser().parse(request)
        configuration_serializer = ConfigurationSerializer(data=configuration_data)
        if configuration_serializer.is_valid():
            configuration_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        configuration_data = JSONParser().parse(request)
        configuration=Configuration.objects.get(ConfigurationId=configuration_data['ConfigurationId'])
        configuration_serializer=ConfigurationSerializer(configuration,data=configuration_data)
        if configuration_serializer.is_valid():
            configuration_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
         configuration=Configuration.objects.get(ConfigurationId=id)
         configuration.delete()
         return JsonResponse("Deleted Succeffully!!", safe=False)