from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')
    timestamp = models.DateTimeField(default= timezone.now)

    class Meta:
        ordering = ['timestamp']

class ProfileType(models.Model):
    profile_type = models.CharField(max_length=100, blank=False, default='')
    timestamp = models.DateTimeField(default= timezone.now)
    
    class Meta:
        ordering = ['timestamp']

class Profile(models.Model):
    user_data = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    profile_type = models.OneToOneField(ProfileType, on_delete=models.CASCADE, default=1)
    authentication_token  = models.CharField(max_length=100,  null=True)
    avatar_url  = models.CharField(max_length=100, default='')
    permissions = models.CharField(max_length=100, null=True)
    timestamp = models.DateTimeField(default= timezone.now)
    
    class Meta:
        ordering = ['timestamp']


