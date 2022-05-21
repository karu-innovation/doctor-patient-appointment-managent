from django.db import models
import uuid
from users.models import Account

time_slot = [
    (1, '8:00-8:30'),
    (2, '8:45-9:15'),
    (3, '9:30-10:00'),
    (4, '10:15-10:45'),
    (5, '11:00-11:30'),
    (6, '11:45-12:15'),
    (7, '12:30-1:00'),
    (8, '2:00-2:30'),
    (9, '2:45-3:15'),
    (10, '3:30-4:00'),
    (11, '4:15-4:45'),
    (12, '5:00-5:30'),
]

# Create your models here.
class Appointment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name='patient')
    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name='appointment_doctor')
    time_slot = model   s.IntegerField(choices=time_slot, null=True, blank=True)
    


    def __str__(self):
        return self.patient.username

    class Meta:
        db_table = 'appointments'
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
