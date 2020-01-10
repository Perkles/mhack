import requests, json
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from urllib import parse

from authentication.models import User
from authentication.serializer import UserSerlializer

from githubapi.profile_creation import create_userprofile_with_github_user_info

class CreateProfile(APIView):

    @method_decorator(csrf_exempt)
    def get(self, request, format=None):

        if (request.session.get('username') == 'new_user' and request.session.get('login_method') == 'githuboauth'):
            create_userprofile_with_github_user_info(request)
        return Response(status=status.HTTP_201_CREATED)


