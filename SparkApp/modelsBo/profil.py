from django.db import models
import uuid




class Profil(models.Model):
    ProfilId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, null=False)
    ProfilName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoProfilFileName = models.CharField(max_length=100)

    #details sur la personne
    #profilDetailPersonne_FK_ID = models.ForeignKey('ProfilDetailPersonne', on_delete=models.CASCADE,  null=False, default=str(uuid.uuid4()))  FK one

    ##configuration
    #configuration_FK_ID = models.ForeignKey('Configuration', on_delete=models.CASCADE,  null=False, default=str(uuid.uuid4()))                 FK one

    ##profilCommercialSpark
    #profilCommercialSpark_FK_ID = models.ForeignKey('ProfilCommercialSpark', on_delete=models.CASCADE,  null=False, default=str(uuid.uuid4())) FK one


    #relation_FK_ID = models.ForeignKey('Relation', on_delete=models.CASCADE, unique=True,  default=str(uuid.uuid4()))                          FK one
    #invitation_FK_ID = models.ForeignKey('Invitations', on_delete=models.CASCADE, null=True) 
    #equipe_FK_ID = models.ForeignKey('Equipe', on_delete=models.CASCADE, null=True)
    #sport_FK_tID = models.ForeignKey('Sport', on_delete=models.CASCADE, null=True)
    #magasin_FK_ID = models.ForeignKey('Magasin', on_delete=models.CASCADE, null=True)
    #publications_FK_ID = models.ForeignKey('Publications', on_delete=models.CASCADE, null=True)
    #ecole_FK_ID = models.ForeignKey('Ecole', on_delete=models.CASCADE, null=True)
    #groupe_FK_ID = models.ForeignKey('Groupe', on_delete=models.CASCADE, null=True)
    ##evenement_FK_ID = models.ForeignKey('Evenement', on_delete=models.CASCADE)
    #media_FK_ID = models.ForeignKey('Media', on_delete=models.CASCADE, null=True)
    #club_FK_ID =  models.ForeignKey('Club', on_delete=models.CASCADE, null=True)




#class ProfilDetailPersonne(models.Model):
#    ID  = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True)
#    age = models.IntegerField(null=False)
#    telephone = models.CharField(max_length=100)
#    adresse = models.ForeignKey('Adresse',  on_delete=models.CASCADE)
#    job = models.CharField(max_length=100)
#    sitewebPersonnel = models.URLField(blank=True)
#    #production_utilisateur = models.ForeignKey('ProductionUtilisateur',  on_delete=models.CASCADE)


#class ProfilCommercialSpark(models.Model):
#    ID  = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=True)


