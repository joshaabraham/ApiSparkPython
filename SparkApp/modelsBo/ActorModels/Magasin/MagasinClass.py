from django.db import models
import uuid

class Magasin(models.Model):
    MagasinId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
