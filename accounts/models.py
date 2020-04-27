from django.db import models
from django.contrib.auth.models import User
Gender = (
    ('male', 'male'),
    ('Female', 'Female'),
    ('Othere', 'Othere'),
)
# Create your models here.


class Registrations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=20)
    gender = models.CharField(max_length=100, choices=Gender)
