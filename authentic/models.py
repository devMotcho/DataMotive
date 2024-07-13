from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import (
    post_save
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='users/', null=True, default='default_img.jpg')

    def __str__(self):
        return f'{self.user.username}'


@receiver(post_save, sender=User)
def profile_post_save(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)