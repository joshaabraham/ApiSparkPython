
from django.conf.urls import url
from SparkApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^authentification/$',views.authentificationApi),
    url(r'^authentification/([0-9]+)$',views.authentificationApi),
   # url(r'^auth/$', views.getAuthenticated),

    url(r'^profil/$',views.profilApi),
    url(r'^profil/([0-9]+)$',views.profilApi),

    url(r'^configuration/$',views.configurationApi),
    url(r'^configuration/([0-9]+)$',views.configurationApi),

    # file URLs
    url(r'^SaveFile$', views.SaveFile)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)