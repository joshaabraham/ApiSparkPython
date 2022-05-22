

from django.db import models
import uuid

class Room(models.Model):
    roomId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

