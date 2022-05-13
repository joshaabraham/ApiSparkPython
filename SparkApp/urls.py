
from django.conf.urls import url
# a deplacer dans un nouveau dossier urls #from SparkApp.Views import ctrl_Authentication

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from SparkApp.Views import authentificationApi , profilApi, configurationApi , saveFile
from SparkApp.views import *


urlpatterns=[
  


    url(r'^authentification/$', authentificationApi),
    url(r'^authentification/([0-9]+)$', authentificationApi),
   # url(r'^auth/$', views.getAuthenticated),

    url(r'^profil/$',profilApi),
    url(r'^profil/([0-9]+)$',profilApi),

    url(r'^configuration/$',configurationApi),
    url(r'^configuration/([0-9]+)$',configurationApi),

    # file URLs
    url(r'^SaveFile$', saveFile)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)