
from django.db import models
import uuid



class ConfigurationProfil(models.Model):
    configurationProfilID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
