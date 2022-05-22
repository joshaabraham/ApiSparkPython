from django.db import models
import uuid

from django.db.models.signals import post_save

class Authentification(models.Model):
    userId  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    motdepasse = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def create_authentification(sender, instance, created, **kwargs):
        if created:
            SparkUser._prefetched_objects_cache.create(user=instance)
            print('Authentification created!')

post_save.connect(create_authentification, sender=Authentification)

def update_authentification(sender, instance, created, **kwargs):
        if created == False:
                instance.profile.save()
                print('Authentification updated!')

post_save.connect(update_authentification, sender=Authentification)