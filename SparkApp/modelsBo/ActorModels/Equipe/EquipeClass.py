from django.db import models
import uuid

class Equipe(models.Model):
    EquipeId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
