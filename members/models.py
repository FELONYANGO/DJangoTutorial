from django.db import models
from django.utils import timezone

# Create your models here.
class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone=models.IntegerField(null=True)
    joined_date=models.DateTimeField(null=True)