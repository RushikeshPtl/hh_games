# Generated by Django 3.2.4 on 2022-07-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_rename_participant_id_room_client_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='client_id',
            field=models.IntegerField(null=True),
        ),
    ]
