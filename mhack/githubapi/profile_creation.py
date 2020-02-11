import requests, json
from login.models import User, Profile
from mpuppet.dict_handdler import extract_from
from rest_framework.response import Response
from rest_framework import status

def create_userprofile_with_github_user_info(request):

    headers = {'Authorization': '{} {}'.format(request.session.get('token_type'), request.session.get('access_token'))}
    json_response = requests.get('https://api.github.com/user', headers=headers).json()
    
    github_id = extract_from(json_response, "id")
    name = extract_from(json_response, "name")
    avatar_url = extract_from(json_response, "avatar_url")
    email = extract_from(json_response, "email")

    print("github id {} - name {} - avatar_url {} - email {}".format(github_id, name, avatar_url, email))
    
    try:
        new_user = User() 
        new_user.authentication_id = github_id
        new_user.name = name
        new_user.email = email
        new_user.save()

        new_profile = Profile()
        new_profile.user_id = new_user.id
        new_profile.avatar_url = avatar_url

        new_profile.User = new_user
        new_profile.save()
        request.session['username'] = name

        content = {'githubapi.profile_creation': 'User created and Profille authomatic filled with user Github public information'}
        return Response(content, status=status.HTTP_201_CREATED)
    except:
        content = {'githubapi.profile_creation': 'something went bad'}
        return Response(content, status=status.HTTP_409_CONFLICT)


