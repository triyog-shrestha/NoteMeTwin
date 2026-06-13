from django.db import models
from django.utils import timezone

class Note(models.Model):
    title = models.TextField(max_length=30)
    content = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title