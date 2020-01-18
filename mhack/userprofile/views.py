import requests, json
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from urllib import parse

from authentication.models import User
from authentication.serializer import UserSerlializer, ProfileSerializer

from githubapi.profile_creation import create_userprofile_with_github_user_info
from django.forms.models import model_to_dict

class CreateProfile(APIView):

    @method_decorator(csrf_exempt)
    def get(self, request, format=None):

        if (request.session.get('username') == 'new_user' and request.session.get('login_method') == 'githuboauth'):
            response = create_userprofile_with_github_user_info(request)
        
        content = {'githubapi.profile_creation': 'User already registred'}
        return Response(content, status=status.HTTP_409_CONFLICT)

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        if (request.session.get('login_method') == 'githuboauth'):
            pass
        elif(request.session.get('login_method') == 'manual'):
            user = User.objects.get(id=request.session.get('user_id'))
            user = model_to_dict(user, fields=[field.name for field in user._meta.fields])
            if 'timestamp' in user:
                del user['timestamp']
            print (user)
            user_serializer = UserSerlializer(data = user)
            if user_serializer.is_valid(raise_exception=True):
                print({user_serializer.data, request.data})
                serializer = ProfileSerializer(data={user_serializer.data, request.data})
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


