
from django.db import models
import uuid

class Notification(models.Model):
    notificationID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  