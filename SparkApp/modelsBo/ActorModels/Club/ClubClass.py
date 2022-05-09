from django.db import models
import uuid

class Club(models.Model):
    ClubId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  

