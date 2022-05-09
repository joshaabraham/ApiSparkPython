
from django.db import models
import uuid

class GeoCoordinates(models.Model):
    GeoCoordinatesID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
   
