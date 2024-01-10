from django.db import models
import uuid


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    email = models.EmailField()
    head = models.UUIDField(default=uuid.uuid4, blank=False, unique=False, null=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.full_name
