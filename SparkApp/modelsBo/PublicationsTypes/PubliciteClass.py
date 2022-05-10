

from django.db import models
import uuid

class Publicite(models.Model):
    publiciteID  = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True)