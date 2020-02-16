import requests, json
from login.models import User, Profile
from mpuppet.dict_handdler import get_gh_authentication_token, extract_from

class Authenticate():

    def __init__(self, code_response, request, token_type = '', access_token = '', name = ''):

        response = requests.post("https://github.com/login/oauth/access_token", data = {
            'client_id': 'dc885fbf11d3232616bc',
            'client_secret': '6bb1a09b2fb453361749919763051b71643ba20f',
            'code': code_response
        })
        access_token, token_type = get_gh_authentication_token(response)

        self.code_response = code_response
        self.token_type = token_type
        self.access_token = access_token
        self.request = request
        self.name = name

    def user_exists(self):
        headers = {'Authorization': '{} {}'.format(self.token_type, self.access_token)}
        response = requests.get('https://api.github.com/user', headers=headers).json()

        id = extract_from(response, 'id')
        
        try:
            User.objects.get(authentication_id=id)
        except User.DoesNotExist:
            return False
        return True

    def mark_as_a_new_user(self):
        self.request.session['access_token'] = self.access_token
        self.request.session['token_type'] = self.token_type
        self.request.session['username'] = 'new_user'
        self.request.session['login_method'] = 'githuboauth'
        print('new user')

    def login(self):
        headers = {'Authorization': '{} {}'.format(self.token_type, self.access_token)}
        response = requests.get('https://api.github.com/user', headers=headers).json()

        name = extract_from(response, 'name')

        self.request.session['access_token'] = self.access_token
        self.request.session['token_type'] = self.token_type
        self.request.session['login_method'] = 'githuboauth'
        self.request.session['username'] = name
        print('logged in')