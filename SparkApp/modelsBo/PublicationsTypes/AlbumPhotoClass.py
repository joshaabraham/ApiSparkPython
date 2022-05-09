
from django.db import models
import uuid

class AlbumPhoto(models.Model):
    AlbumPhotoID  = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True)