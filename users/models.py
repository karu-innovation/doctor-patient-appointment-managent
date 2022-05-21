import uuid

from django.forms import CharField
from specialisation.models import Specialisation
from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    class Meta:
        pass

    def __str__(self):
        return self.username


class Doctor(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True, related_name='doctor')
    specialisation = models.ForeignKey(Specialisation, 
                                    on_delete=models.CASCADE, 
                                    null=True, 
                                    blank=True, 
                                    related_name='doctor')
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)

    class Meta:
        db_table = 'doctors'
    
    def __str__(self):
        return self.user.username
