import requests, json

from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .authenticate import *
from urllib import parse

from authentication.models import User
from authentication.serializer import UserSerlializer

class ManualUserRegistration(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        serializer = UserSerlializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GithubRegistration(APIView):
    def get(self, request, format=None):
        # List of things that this URL is in charge of:
        #     log in with github
        #     verify if user is already registred

        # Callback function to https://github.com/login/oauth/authorize?client_id=dc885fbf11d3232616bc
        # if the user logs in successfully in Github the callback should return a query param named
        # code.
        code_response = self.request.query_params.get('code')

        # The code, which expires in 10 minutes, is sent back to Github with additional information about
        # our OAuth app (client_id, client_secret). If all information is valid the user is logged
        # https://developer.github.com/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/
        # https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/
        response = requests.post("https://github.com/login/oauth/access_token", data = {
            'client_id': 'dc885fbf11d3232616bc',
            'client_secret': 'a9d70f98b5bd165cbe45f9b767a9869e25792587',
            'code': code_response
        })

        # Lack refatoration, that code may be in a package 
        access_token = ''
        token_type = ''
        response_dic = parse.parse_qs(parse.urlsplit(response.text).path)
        for key, value in response_dic.items():
            if (key == 'access_token'):
                access_token = str(value).replace('[', '').replace("'", '').replace("]", '')
            elif (key == 'token_type'):
                token_type = str(value).replace('[', '').replace("'", '').replace("]", '')
        # Seriously though

        if response.status_code == 200:
            if(verify_new_user(token_type, access_token)):
                set_access_token()
            else:
                register_new_user()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)



# class FetchAndCreateUsers(APIView):

#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = UserSerlializer(users, many=True)
#         return Response(serializer.data)

#     @method_decorator(csrf_exempt)
#     def post(self, request, format=None):
#         serializer = UserSerlializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class Test_detail(APIView):

#     def get_object(self, pk):
#         try:
#             return Test.objects.get(pk=pk)
#         except Test.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         test = self.get_object(pk)
#         serializer = TestSerializer(test)
#         return Response(serializer.data)

#     @method_decorator(csrf_exempt)
#     def put(self, request, pk, format=None):
#         test = self.get_object(pk)
#         serializer = TestSerializer(test, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     @method_decorator(csrf_exempt)
#     def delete(self, request, pk, format=None):
#         test = self.get_object(pk)
#         test.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

