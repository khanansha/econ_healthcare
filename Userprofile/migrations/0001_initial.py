# Generated by Django 2.2.10 on 2020-04-13 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOB', models.DateField()),
                ('Height', models.IntegerField(default=170)),
                ('Weight', models.IntegerField(default=170)),
                ('Do_you_Smoke', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100)),
                ('Do_you_Consume_Alcohol', models.CharField(choices=[('Frequently', 'Frequently'), ('Socially', 'Socially'), ('No', 'No')], max_length=100)),
                ('Allergy', models.TextField()),
                ('Current_Medication', models.TextField()),
                ('Blood_Group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
