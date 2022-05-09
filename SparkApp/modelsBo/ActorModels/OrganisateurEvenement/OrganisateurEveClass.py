from django.db import models
import uuid

class OrganisateurEve(models.Model):
    OrganisateurEveId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
