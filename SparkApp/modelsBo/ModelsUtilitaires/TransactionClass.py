

from django.db import models
import uuid
from enum import Enum
# quand on fait une requete monnaitaire, d'inscritpion de changement d'Abonnement etc ... un status de la transaction est affichee pour savoir ou en est le traitement de la requete.


class Transaction(models.Model):
    transactionID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    PublishDay = models.CharField(max_length=4, choices=[(tag, tag.value) for tag in StatusSubClass])


class StatusSubClass(Enum):
    RS = "Request sent"
    P = "Pending"
    Err = "Error"
    C = "Completed"
    Can = "Cancelled"