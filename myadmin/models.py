from django.db import models

class Announcements(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    writer = models.PositiveIntegerField()
    is_important = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)

