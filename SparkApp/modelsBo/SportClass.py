from django.db import models
import uuid


class Sport(models.Model):
    sportID  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)