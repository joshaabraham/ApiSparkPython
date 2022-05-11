
from ..ActorModels.Auteur.AuteurClass import Auteur

from django.db import models
import uuid

class Article(models.Model):
    articleID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    #ForeignKeys
    auteur_fk = models.ForeignKey(Auteur, null = True, on_delete=models.SET_NULL)
   
   