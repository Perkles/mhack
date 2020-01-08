from django.db import models

class User(models.Model):
    name = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100, blank=False, default='')
    password = models.CharField(max_length=100, blank=False, default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

class Type(models.Model):
    profile_type = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_type = models.OneToOneField(Type, on_delete=models.CASCADE)
    authentication_code  = models.CharField(max_length=100)
    avatar_url  = models.CharField(max_length=100)
    permissions = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']


