from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .modelsBo import Authentification, Profil
from SparkApp.serializers import *

from django.core.files.storage import default_storage

from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response


from django.contrib.auth.models import User



# for payment
import stripe
from django.http import JsonResponse
#from SparkApi.settings import settings


from SparkApp.Views import *

# for payment
stripe.api_key = ''
#stripe.api_key = setting.STRIPE_SECRET_KEY



# Create your views here.


#
   