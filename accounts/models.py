from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class User(User):
    is_kandidat = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    phone = PhoneNumberField(null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)


class Kandidat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Hr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
