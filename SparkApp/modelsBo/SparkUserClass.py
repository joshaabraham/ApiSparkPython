from django.db import models
import uuid



from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser, User

from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save





class SparkUser(models.Model):

    sparkuserID  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    #profil_fk
    #configuration_fk

    def __str__(self):
        return str(self.user_id)


#@receiver(post_save, sender=SparkUser)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        Token._prefetched_objects_cache.create(user=instance)


#def create_sparkUser(sender, instance, created, **kwargs):
#        if created:
#            SparkUser._prefetched_objects_cache.create(user=instance)
#            print('SparkUser created!')

#post_save.connect(create_sparkUser, sender=User)

#def update_sparkUser(sender, instance, created, **kwargs):
#        if created == False:
#                instance.profile.save()
#                print('SparkUser updated!')

#post_save.connect(update_sparkUser, sender=User)

@receiver(post_save, sender=SparkUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
