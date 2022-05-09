from django.db import models
import uuid

class Auteur(models.Model):
    AuteurId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  


