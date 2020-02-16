from django.test import TestCase
import requests, json
from githubapi.authenticate import Authenticate
from mpuppet.dict_handdler import extract_from

class AuthenticateTestCase(TestCase):
    # def setUp(selt):
    #     User.objects.create(
    #         name = 'Leroy Jenkins',
    #         authentication_id = '',
    #         email = '',
    #         password = ''
    #     )

    def test_github_authorize_url_callback(self):
        response = requests.get('https://github.com/login/oauth/authorize?client_id=dc885fbf11d3232616bc')
        self.assertNotEqual(response, "<Response [200]>")

# class ProfileTestCAse(TestCase):
#     def setUp(self):
#         User.objects.create(
#             id= 1,
#             name = 'Leroy Jenkins',
#             authentication_id = '',
#             email = '',
#             password = ''
#         )

#     def test_profile_creation(self):
#         new_profile = Profile() 
#         new_profile.user = User.objects.get(id=1)
#         new_profile.type = 'TM'
#         new_profile.email = 'leroy@jenkins.com'
#         new_profile.avatar_url = 'http://jenkins.com/pictures/leroy/1'
#         new_profile.save()
#         self.assertTrue(new_profile != "" ,"Profile should be created sucessfully")     