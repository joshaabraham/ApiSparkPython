from django.db import models
import uuid

class Relation(models.Model):
    relationID = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True)
