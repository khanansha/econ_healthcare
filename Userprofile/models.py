from django.db import models

from django.contrib.auth.models import User

# Create your models here.
select = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)
select_Consume_Alcohol = (
    ('Frequently', 'Frequently'),
    ('Socially', 'Socially'),
    ('No', 'No'),
)
select_bloodgroup = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    DOB = models.DateField(null=True)
    Height = models.CharField(max_length=100, null=True)
    Weight = models.CharField(max_length=100, null=True)
    Smoke = models.CharField(max_length=100, choices=select, null=True)
    Alcohol = models.CharField(
        max_length=100, choices=select_Consume_Alcohol, null=True)
    Allergy = models.TextField(null=True)
    Current_Medication = models.TextField(null=True)
    Blood_Group = models.CharField(
        max_length=100, choices=select_bloodgroup, null=True)
