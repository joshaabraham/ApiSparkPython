from django.db import models
import uuid



class Adresse(models.Model):
   
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    n_indic = models.CharField(max_length=255)
    no_rue = models.IntegerField()
    nom_rue = models.CharField(max_length=255)
    code_postal = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    pays = models.CharField(max_length=255)
