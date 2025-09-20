from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post


@receiver(post_save, sender=Post)
def increase_views(sender, instance, created, **kwargs):
    if created:
        print(f"New Post Created : {instance.title}")