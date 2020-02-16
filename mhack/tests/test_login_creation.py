from django.test import TestCase
import requests, json
from githubapi.authenticate import Authenticate
from mpuppet.dict_handdler import extract_from

class AuthenticateTestCase(TestCase):

    def test_github_authorize_url_callback(self):
        response = requests.get('https://github.com/login/oauth/authorize?client_id=dc885fbf11d3232616bc')
        self.assertTrue(response.status_code == 200, "Client_id dont match, check application credentials.")  