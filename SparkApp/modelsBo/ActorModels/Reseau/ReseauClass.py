from django.db import models
import uuid

class Reseau(models.Model):
    ReseauId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
