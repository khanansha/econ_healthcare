# Generated by Django 2.2.10 on 2020-04-13 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Do_you_Consume_Alcohol',
            new_name='Alcohol',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Do_you_Smoke',
            new_name='Smoke',
        ),
    ]