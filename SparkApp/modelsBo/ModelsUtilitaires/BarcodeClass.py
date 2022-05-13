
from django.db import models
import uuid

class Barcode(models.Model):
    barcodeID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   
