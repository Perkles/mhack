import requests, json
from authentication.models import User

def verify_new_user(token_type, access_token):
    id = ''
    headers = {'Authorization': '{} {}'.format(token_type, access_token)}
    response = requests.get('https://api.github.com/user', headers=headers).json()

    # That could be encapsulated
    for key, value in response.items():
        if (key == 'id'):
            id = value

    try:
        User.objects.get(pk=id)
        return True
    except User.DoesNotExist:
        return False

def register_new_user():
    print('new user')

def set_access_token():
    print('already registred user')