from django.test import TestCase
from login.models import User, Profile
from django.utils import timezone

class UserTestCase(TestCase):
    def setUp(selt):
        User.objects.create(
            name = 'Leroy Jenkins',
            authentication_id = '',
            email = '',
            password = ''
        )

    def test_user_creaion(self):
        user = User.objects.get(name='Leroy Jenkins')
        self.assertIsNotNone(user, "User should be created sucessfully")

class ProfileTestCAse(TestCase):
    def setUp(self):
        User.objects.create(
            id= 1,
            name = 'Leroy Jenkins',
            authentication_id = '',
            email = '',
            password = ''
        )

    def test_profile_creation(self):
        new_profile = Profile() 
        new_profile.user = User.objects.get(id=1)
        new_profile.type = 'TM'
        new_profile.email = 'leroy@jenkins.com'
        new_profile.avatar_url = 'http://jenkins.com/pictures/leroy/1'
        new_profile.save()
        self.assertIsNotNone(new_profile,"Profile should be created sucessfully")     