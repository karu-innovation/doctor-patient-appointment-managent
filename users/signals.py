# import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import Account, Doctor

User = get_user_model()

#create doctor when user is created with is_true
@receiver(post_save, sender=User)
def create_doctor(sender, instance, created, **kwargs):
    if created and instance.is_doctor:
        Doctor.objects.create(user=instance)
    Token.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_doctor_profile(sender, instance, **kwargs):
    instance.doctor.save()

post_save.connect(create_doctor, sender=User)
post_save.connect(save_doctor_profile, sender=User)

        