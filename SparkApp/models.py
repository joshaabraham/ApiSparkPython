from django.db import models
import uuid

from .modelsBo import * 


from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



# Create your models here.
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#class Authentification(models.Model):
#    userId  = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True)
#    name = models.CharField(max_length=100)
#    email = models.EmailField(max_length=100, unique=True)
#    motdepasse = models.CharField(max_length=100)
#    username = None



    
#class CentreInteret(models.Model):
#    ID  = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True)

#class GroupeDeCommunication(models.Model):
#    ID = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True) # ce sera l'identifiant de la chambre de communication
#    Profil_relie_ID = models.ForeignKey('Profil', on_delete=models.CASCADE, null=True)

#class Evenement(models.Model):
#    ID  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  
#    class Meta:
#       abstract = True

#class Competition(Evenement):
#    ID  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#class RendezVOus(Evenement):
#    ID  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)




#class Club(models.Model):
#    ID  = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True)
#    #nom = models.ForeignKey('Profil', on_delete=models.CASCADE)
#    #description = models.ForeignKey('Profil', on_delete=models.CASCADE)
#    adresse = models.ForeignKey('Adresse', on_delete=models.CASCADE)

#class Media(models.Model):
#    ID  = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True)
#    ID_profil = models.ForeignKey('Profil', on_delete=models.CASCADE)
    #IDalbumPhotos 
    #IDlisteVideos 



#class Relation(models.Model):
#    ID = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True)
    #profil = models.ForeignKey('Profil', on_delete=models.CASCADE)


#class Invitations(models.Model):
#    ID = models.UUIDField(primary_key=True,  default=str(uuid.uuid4()), editable=True)
    #profil = models.ForeignKey('Profil', on_delete=models.CASCADE)


#class Equipe(models.Model):
#    ID  = models.UUIDField(primary_key=True,  default=str(uuid.uuid4()), editable=True)
    #profil = models.ForeignKey('Profil', on_delete=models.CASCADE)


#class Group(models.Model):
#    ID  = models.UUIDField(primary_key=True,  default=str(uuid.uuid4()), editable=True)
    #nom = models.ForeignKey('Profil', on_delete=models.CASCADE)

#class Sport(models.Model):
#    ID  = models.UUIDField(primary_key=True,  default=str(uuid.uuid4()), editable=True)
    #profil = models.ForeignKey('Profil', on_delete=models.CASCADE)



#class Publications(models.Model):
#    ID  = models.UUIDField(primary_key=True,  default=str(uuid.uuid4()), editable=True)
    #illustration
    #titre
    #description
    #contenu
    #datedeCreation
    #derniereMiseAjour


 
#class Ecole(models.Model):
#    ID = models.UUIDField(primary_key=True,  default=str(uuid.uuid4()), editable=True)
    #illustration
    #nom
    #domain
    #sport
    #cours = models.ForeignKey('Cour', on_delete=models.CASCADE)

#class Cour(models.Model):
#    ID  = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True)
#    IDchapitre = models.ForeignKey('Chapitre', on_delete=models.CASCADE)
#    titre = models.CharField(max_length = 255)
#    description = models.CharField(max_length = 450)
#    #prerequis
#    #difficulte
#    duree = models.DurationField()
#    #auteur
   
    
#class Chapitre(models.Model):
#    ID = models.UUIDField(primary_key=True,  default=str(uuid.uuid4()), editable=True)
#    titre = models.CharField(max_length = 255)
#    description = models.CharField(max_length = 450)
#    duree = models.DurationField()







#@receiver(post_save, sender= settings.AUTH_USER_MODEL)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        Token.objects.create(user=instance)