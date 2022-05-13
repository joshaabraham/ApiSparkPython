


from django.db import models
import uuid



class Payment(models.Model):
    paymentID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

   