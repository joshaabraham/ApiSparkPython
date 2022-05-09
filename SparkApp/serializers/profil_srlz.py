from rest_framework import serializers
from SparkApp.modelsBo import  Profil
from django.contrib.auth.models import User, Group

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ('ProfilId',
                    #'ProfilName',
                    #'Department',
                    #'DateOfJoining',
                    #'PhotoProfilFileName',

                    ##details sur la personne
                    #'profilDetailPersonne_FK_ID',

                    ##configuration
                    #'configuration_FK_ID',

                    ##profilCommercialSpark
                    #'profilCommercialSpark_FK_ID',


                    #'relation_FK_ID',
                    #'invitation_FK_ID',
                    #'equipe_FK_ID',
                    #'sport_FK_tID',
                    #'magasin_FK_ID',
                    #'publications_FK_ID',
                    #'ecole_FK_ID',
                    #'groupe_FK_ID',
                    ##evenement_FK_ID = models.ForeignKey('Evenement', on_delete=models.CASCADE)
                    #'media_FK_ID',
                    #'club_FK_ID'
                    )
