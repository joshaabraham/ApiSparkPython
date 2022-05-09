from django.db import models
import uuid

class MediaVideo(models.Model):
    videoID  = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True)