# Generated by Django 2.2.4 on 2019-08-09 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
