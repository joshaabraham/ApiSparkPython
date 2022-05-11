from django.db import models
import uuid



from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(models.Model):
    userID  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)

    #profil_fk
    #configuration_fk
 


