from django.db import models
import uuid

class GroupeDeCommunication(models.Model):
    groupeDeCommunicationId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

