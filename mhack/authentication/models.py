from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    email = models.CharField(max_length=100, blank=False, default='')
    password = models.CharField(max_length=100, blank=False, default='')
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['timestamp']

class Type(models.Model):
    profile_type = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_type = models.OneToOneField(Type, on_delete=models.CASCADE,  null=True)
    authentication_token  = models.CharField(max_length=100,  null=True)
    avatar_url  = models.CharField(max_length=100, default='')
    permissions = models.CharField(max_length=100, null=True)
    timestamp = models.DateTimeField(auto_now_add=True,  null=True)
    
    class Meta:
        ordering = ['timestamp']

