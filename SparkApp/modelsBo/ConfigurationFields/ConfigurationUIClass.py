
from django.db import models
import uuid



class ConfigurationUI(models.Model):
    configurationUI_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
