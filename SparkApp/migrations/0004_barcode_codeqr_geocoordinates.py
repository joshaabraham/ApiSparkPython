# Generated by Django 3.2.13 on 2022-05-13 18:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('SparkApp', '0003_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('barcodeID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CodeQR',
            fields=[
                ('codeQRID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='GeoCoordinates',
            fields=[
                ('GeoCoordinatesID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
