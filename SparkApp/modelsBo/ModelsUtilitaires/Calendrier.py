
from django.db import models
import uuid

class Calendrier(models.Model):
    calendrierID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   
   