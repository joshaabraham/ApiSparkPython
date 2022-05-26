from django.db import models
import uuid

class Produit(models.Model):
    produitId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100)
    prix = models.IntegerField(default=0)
    file = models.FileField(upload_to="product_files/", blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return self.nom
    
    def get_display_price(self):
        return "{0:.2f}".format(self.prix / 100)