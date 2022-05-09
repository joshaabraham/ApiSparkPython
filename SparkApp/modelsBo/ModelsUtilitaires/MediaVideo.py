from django.db import models
import uuid

class Video(models.Model):
    videoID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  