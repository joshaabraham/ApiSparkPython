
from django.db import models
import uuid

class Group(models.Model):
    groupID  = models.UUIDField(primary_key=True,  default=uuid.uuid4, editable=True)
