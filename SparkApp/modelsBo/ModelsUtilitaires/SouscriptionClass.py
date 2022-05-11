

from django.db import models
import uuid



class Souscription(models.Model):
    SouscriptionID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

   