

from django.db import models
import uuid


class Ecole(models.Model):
    EcoleID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)