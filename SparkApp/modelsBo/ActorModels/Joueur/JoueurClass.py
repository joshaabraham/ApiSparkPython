from django.db import models
import uuid

class Joueur(models.Model):
   JoueurId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
