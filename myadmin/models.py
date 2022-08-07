from tkinter import CASCADE
from django.db import models
from users.models import User
class Announcements(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    is_important = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    

