from django.db import models
from authentication.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save
#from hospital.models import Hospital


# Create your models here.

class Hospital(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,  on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, default="Hospital Name")
    country = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.name



#hospital created on account verification just with this signals no need for additional config
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Hospital.objects.create(user=instance)
        print("hospital created")


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.hospital.save()
        print('hospital updated')

