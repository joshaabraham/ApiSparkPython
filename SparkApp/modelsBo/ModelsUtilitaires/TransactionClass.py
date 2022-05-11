

from django.db import models
import uuid

# quand on fait une requete monnaitaire, d'inscritpion de changement d'Abonnement etc ... un status de la transaction est affichee pour savoir ou en est le traitement de la requete.

class Transaction(models.Model):
    transactionID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

   
