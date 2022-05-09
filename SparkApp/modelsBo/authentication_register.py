from django.db import models
import uuid

class Authentification(models.Model):
    userId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    motdepasse = models.CharField(max_length=100)

