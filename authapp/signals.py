from django.db.models.signals import save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserRegistrationModel

@receiver(post_save, sender = User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        profile = UserRegistrationModel.objects.create(user=instance)
        profile.save()