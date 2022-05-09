from django.db import models
import uuid

class Publications(models.Model):
    ID  = models.UUIDField(primary_key=True,  default=str(uuid.uuid4()), editable=True)
        #illustration
    #titre
    #description
    #contenu
    #datedeCreation
    #derniereMiseAjour