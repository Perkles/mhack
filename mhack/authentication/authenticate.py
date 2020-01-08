import requests, json
from authentication.models import User, Profile

def user_exists(token_type, access_token):
    id = ''
    headers = {'Authorization': '{} {}'.format(token_type, access_token)}
    response = requests.get('https://api.github.com/user', headers=headers).json()
    print(response)
    # That could be encapsulated
    for key, value in response.items():
        if (key == 'id'):
            id = value
    try:
        User.objects.get(id=id)
    except User.DoesNotExist:
        return False
    return True

def mark_as_a_new_user(request, token_type, access_token):
    request.session['access_token'] = access_token
    request.session['token_type'] = token_type
    request.session['username'] = 'new_user'
    request.session['login_method'] = 'githuboauth'

def login(request, token_type, access_token):
    request.session['access_token'] = access_token
    request.session['token_type'] = token_type
    request.session['login_method'] = 'githuboauth'