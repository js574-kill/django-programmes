
from django.db import models
import uuid

class Identite(models.Model):
    id = models.AutoField(primary_key=True)
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    lastName = models.CharField(max_length=120)
    firstName = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    postalZip = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=60, blank=True, null=True) 
    company = models.CharField(max_length=200, blank=True, null=True)
    publicUrl = models.URLField(blank=True, null=True)
    creditCard = models.CharField(max_length=50, blank=True, null=True)
    cvv = models.PositiveIntegerField(blank=True, null=True)
    pin = models.PositiveIntegerField(blank=True, null=True)
    amount = models.CharField(max_length=50, blank=True, null=True)
    cars = models.PositiveSmallIntegerField(default=0)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName} ({self.company})"
