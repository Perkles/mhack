from django.db import models

class User(models.Model):
    name = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100, blank=False, default='')
    password = models.CharField(max_length=100, blank=False, default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']