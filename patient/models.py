from django.db import models
from authentication.models import User
# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    owner = models.ForeignKey(to=User, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
        


class Card(models.Model):    
    name = models.CharField(max_length=255, null=True)
    card_number = models.CharField(max_length=255, null=True)    
    owner = models.OneToOneField(Patient, null=True, blank=True, on_delete=models.CASCADE)
    hospital = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        



class Diagnoses(models.Model):
    sickness = models.CharField(max_length=255, null=True)
    note = models.TextField(max_length=255, null=True)   
    owner = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.CASCADE)
    hospital = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.sickness
        