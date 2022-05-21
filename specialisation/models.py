from django.db import models

import uuid
# Create your models here.
class Specialisation(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name
    