from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')
    timestamp = models.DateTimeField(default= timezone.now)

    class Meta:
        ordering = ['timestamp']

class Profile(models.Model):

    TEAMLEADER = 'TL'
    TEAMMEMBER = 'TM'
    BUSINESSJURY = 'BJ'
    TECHINCALJURY = 'TJ'
    STAFF = 'ST'
    MANAGER = 'MG'

    PROFILE_CHOICES = [
        (TEAMLEADER, 'Team Leader'),
        (TEAMMEMBER, 'Team Member'),
        (BUSINESSJURY, 'Business Jury'),
        (TECHINCALJURY, 'Techincal Jury'),
        (STAFF, 'Staff'),
        (MANAGER, 'Manager'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_type = models.CharField(max_length=2,choices=PROFILE_CHOICES,default=TEAMMEMBER)
    authentication_token  = models.CharField(max_length=100,  null=True)
    avatar_url  = models.CharField(max_length=100, default='')
    permissions = models.CharField(max_length=100, null=True)
    timestamp = models.DateTimeField(default= timezone.now)

    # def is_upperclass(self):
    #     return self.profile_type in {self.JUNIOR, self.SENIOR}

    class Meta:
        ordering = ['timestamp']


