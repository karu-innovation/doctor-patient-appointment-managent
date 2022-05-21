import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    specialization = models.ForeignKey('specialisation.Specialisation', on_delete=models.CASCADE, 
                            null=True, 
                            blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    class Meta:
        pass

    def __str__(self):
        return self.username
    
