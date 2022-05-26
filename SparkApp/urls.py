
from django.conf.urls import url
from django.urls import include, path
# a deplacer dans un nouveau dossier urls #from SparkApp.Views import ctrl_Authentication

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
5
from SparkApp.views import *

from SparkApp.Views import *

#from SparkApp.views import CreateCheckoutSession

from rest_framework.authtoken import views
from django.contrib.auth.views import auth_login

urlpatterns=[

    path('login/', auth_login, name='login'),
    path('register/', authentificationRegister, name='register'),

    url(r'authentification/$', authentificationApi),
    url(r'authentification/([0-9]+)$', authentificationApi),
    url(r'authentification/register/', authentificationRegister),
    url(r'authentification/login/$', authentificationLogin),
   # url(r'^auth/$', views.getAuthenticated),

    url(r'profil/$',profilApi),
    url(r'profil/([0-9]+)$',profilApi),

    url(r'configuration/$',configurationApi),
    url(r'configuration/([0-9]+)$',configurationApi),

    path("get-details",UserDetailAPI.as_view()),
    path('register',RegisterUserAPIView.as_view()),

   #path('create-checkout-session', CreateCheckoutSession.as_view(), name='create-checkout-session'),

    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    # file URLs
    url(r'SaveFile$', saveFile)

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)