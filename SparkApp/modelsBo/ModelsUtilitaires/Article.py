
from django.db import models
import uuid

class Article(models.Model):
    articleID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   
   