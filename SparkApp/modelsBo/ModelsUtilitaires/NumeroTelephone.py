
from django.db import models
import uuid



class Telephone(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero = models.CharField(max_length=255)
    type_de_numero = models.IntegerField()
   