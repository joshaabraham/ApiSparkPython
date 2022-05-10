# Generated by Django 3.2.8 on 2022-04-19 20:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('SparkApp', '0005_auto_20220418_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumPhoto',
            fields=[
                ('AlbumPhotoID', models.UUIDField(default='1ee655c5-9c48-489a-ad39-8e9bd76e7ec0', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('articleID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Calendrier',
            fields=[
                ('calendrierID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='EntreprisePublicitaire',
            fields=[
                ('EPPId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='HashWords',
            fields=[
                ('hashWordsID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('invitationID', models.UUIDField(default='adf88fa2-fb1a-402d-8601-1b4bf7722b9f', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Joueur',
            fields=[
                ('JoueurId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MediaVideo',
            fields=[
                ('videoID', models.UUIDField(default='8bbe52f1-2c34-4889-ba7e-017d49eed049', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrganisateurEve',
            fields=[
                ('OrganisateurEveId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Publicite',
            fields=[
                ('publiciteID', models.UUIDField(default='6579a572-6d15-46e8-8e05-c701721d1fce', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reseau',
            fields=[
                ('ReseauId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('videoID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='cour',
            name='IDchapitre',
        ),
        migrations.RemoveField(
            model_name='media',
            name='ID_profil',
        ),
        migrations.RemoveField(
            model_name='profildetailpersonne',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='centreinteret',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='club',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='club',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='ecole',
            name='cours',
        ),
        migrations.RemoveField(
            model_name='equipe',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='group',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='groupedecommunication',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='groupedecommunication',
            name='Profil_relie_ID',
        ),
        migrations.RemoveField(
            model_name='magasin',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='club_FK_ID',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='configuration_FK_ID',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='ecole_FK_ID',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='equipe_FK_ID',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='groupe_FK_ID',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='invitation_FK_ID',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='magasin_FK_ID',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='media_FK_ID',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='profilCommercialSpark_FK_ID',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='profilDetailPersonne_FK_ID',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='publications_FK_ID',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='relation_FK_ID',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='sport_FK_tID',
        ),
        migrations.RemoveField(
            model_name='relation',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='ID',
        ),
        migrations.AddField(
            model_name='centreinteret',
            name='centreInteretId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='club',
            name='ClubId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='equipe',
            name='EquipeId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='group',
            name='groupID',
            field=models.UUIDField(default='b648b790-22ca-45e3-aa62-fd635fcc2b04', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='groupedecommunication',
            name='groupeDeCommunicationId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='magasin',
            name='MagasinId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='relation',
            name='relationID',
            field=models.UUIDField(default='cb4d66a0-07bc-4b25-a8f8-43614d6af6df', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='sport',
            name='sportID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='ID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ecole',
            name='ID',
            field=models.UUIDField(default='5d7853cd-8dd4-40e7-8a60-5d3f8f080c72', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profil',
            name='ProfilId',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='publications',
            name='ID',
            field=models.UUIDField(default='0a0d3e2f-6de1-4c89-b7d0-21de2319e68f', primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Chapitre',
        ),
        migrations.DeleteModel(
            name='Cour',
        ),
        migrations.DeleteModel(
            name='Groupe',
        ),
        migrations.DeleteModel(
            name='Invitations',
        ),
        migrations.DeleteModel(
            name='Media',
        ),
        migrations.DeleteModel(
            name='ProfilCommercialSpark',
        ),
        migrations.DeleteModel(
            name='ProfilDetailPersonne',
        ),
    ]