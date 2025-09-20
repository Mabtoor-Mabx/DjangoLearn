from django.db import models

class PostManager(models.Manager):
    def popular(self):
        return self.get_queryset().filter(views__gte=10)