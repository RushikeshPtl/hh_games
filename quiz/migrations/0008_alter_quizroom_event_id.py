# Generated by Django 4.0.6 on 2022-08-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_quizroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizroom',
            name='event_id',
            field=models.IntegerField(null=True),
        ),
    ]
