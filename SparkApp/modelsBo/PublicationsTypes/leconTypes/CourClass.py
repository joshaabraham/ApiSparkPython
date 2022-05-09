
from django.db import models
import uuid


class Cour(models.Model):
    courID  = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True)
    #IDchapitre = models.ForeignKey('Chapitre', on_delete=models.CASCADE)
    #titre = models.CharField(max_length = 255)
    #description = models.CharField(max_length = 450)
    ##prerequis
    ##difficulte
    #duree = models.DurationField()
    ##auteur
   