
from django.db import models
import uuid



class ConfigurationGroupe(models.Model):
    configurationGroupeID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)