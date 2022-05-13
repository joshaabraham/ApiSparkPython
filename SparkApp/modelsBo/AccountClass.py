
from django.db import models
import uuid

class Account(models.Model):
    accountId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

