from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg, Count
from django.utils import timezone

from .managers import PostManager
# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.username
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    objects = PostManager() # Custom Manager


    def __str__(self):
        return self.title
