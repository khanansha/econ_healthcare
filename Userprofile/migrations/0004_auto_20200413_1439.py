# Generated by Django 2.2.10 on 2020-04-13 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0003_auto_20200413_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Alcohol',
            field=models.CharField(choices=[('Frequently', 'Frequently'), ('Socially', 'Socially'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Allergy',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Blood_Group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Current_Medication',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='DOB',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Height',
            field=models.IntegerField(default=170, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Smoke',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Weight',
            field=models.IntegerField(default=170, null=True),
        ),
    ]