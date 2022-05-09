
from django.db import models
import uuid

class Invitation(models.Model):
    invitationID = models.UUIDField(primary_key=True,  default=str(uuid.uuid4()), editable=True)
