from django.db import models
import uuid

class EntreprisePublicitaire(models.Model):
    EPPId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
