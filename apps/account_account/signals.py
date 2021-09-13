from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Cashilok, CustomUser


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Cashilok.objects.create(owner=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.cashelok.save()
