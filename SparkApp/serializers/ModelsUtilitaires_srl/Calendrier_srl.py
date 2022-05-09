
from django.db import models
import uuid
from rest_framework import serializers

class Calendrier(models.Model):
    calendrierID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   
   