from django.db import models
import uuid

from .ConfigurationFields import *

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Configuration(models.Model):
    ID  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
   # on prend toutes le infos du profil et on demande si on veut afficher pour tous / pour les contacts des contacts / pour les contacts
   # on demande comment on retrouve la personne
   #viePrivee = models.ForeignKey('Profil', on_delete=models.CASCADE)

    configurationCommerciale_fk = models.ForeignKey(ConfigurationCommerciale, default = None, on_delete=models.SET_DEFAULT)
    configurationProfil_fk = models.ForeignKey(ConfigurationProfil, default = None, on_delete=models.SET_DEFAULT)
    configurationUI_fk = models.ForeignKey(ConfigurationUI, default = None, on_delete=models.SET_DEFAULT)
    configurationGroupe_fk = models.ForeignKey(ConfigurationGroupe, default = None, on_delete=models.SET_DEFAULT)


    #visibilite = models.ForeignKey('Profil', on_delete=models.CASCADE)



