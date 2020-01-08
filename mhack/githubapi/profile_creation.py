import requests, json
from authentication.models import User, Profile

def create_userprofile_with_github_user_info(request):
    access_token = request.session.get('access_token')
    token_type = request.session.get('token_type')

    headers = {'Authorization': '{} {}'.format(token_type, access_token)}
    json_response = requests.get('https://api.github.com/user', headers=headers).json()

    print(json_response)

    github_id = extract_from(json_response, "id")
    name = extract_from(json_response, "name")
    avatar_url = extract_from(json_response, "avatar_url")
    email = extract_from(json_response, "email")

    print("github id {} - name {} - avatar_url {} - email {}".format(github_id, name, avatar_url, email))
    

    new_user = User()
    new_user.id = github_id 
    new_user.email = email

    new_profile = Profile()
    new_profile.user_id = github_id
    new_profile.avatar_url = avatar_url
    
    new_user.save()
    new_profile.save()
    print('whaaaat')


def extract_from(json_response, the_subject):
    for key, value in json_response.items():
        if (key == the_subject):
            return value