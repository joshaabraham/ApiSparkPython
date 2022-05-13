
from django.db import models
import uuid

class CodeQR(models.Model):
    codeQRID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  