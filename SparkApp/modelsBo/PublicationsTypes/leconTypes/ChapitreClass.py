

from django.db import models
import uuid

class Chapitre(models.Model):
    chapitreID = models.UUIDField(primary_key=True,  default=str(uuid.uuid4()), editable=True)
    #titre = models.CharField(max_length = 255)
    #description = models.CharField(max_length = 450)
    #duree = models.DurationField()
