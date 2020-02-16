from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from urllib import parse
import requests, json

from .models import User, Profile
from .serializer import UserSerlializer, ProfileSerializer, LoginSerializer
from githubapi.authenticate import Authenticate
from githubapi.profile_creation import create_userprofile_with_github_user_info


class ManualUserRegistration(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Im repeting this chunk of code everywhere, should encapsulate it
            request.session['username'] = serializer.data.get("name")
            request.session['user_id'] = serializer.data.get("id")
            request.session['login_method'] = 'manual'

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GithubRegistration(APIView):
    def get(self, request, format=None):
        # Callback function to https://github.com/login/oauth/authorize?client_id=dc885fbf11d3232616bc
        # ... if the user logged in github this callback uri receves a param named code.

        code_response = self.request.query_params.get('code')
        authenticate = Authenticate(code_response, request)
        
        if(authenticate.user_exists()):
            authenticate.login()
            return Response(status=status.HTTP_201_CREATED)
        else:
            authenticate.mark_as_a_new_user()
            return Response(status=status.HTTP_201_CREATED)

class Login(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(email= serializer.data.get("email"))
            except User.DoesNotExist:
                return Response("User does not exists", status=status.HTTP_400_BAD_REQUEST)

            if user.password == serializer.data.get("password"):
                request.session['username'] = user.name
                request.session['user_id'] = user.id
                request.session['login_method'] = 'manual'
                return Response("Logged in", status=status.HTTP_200_OK)
            else:
                return Response("Email or password missmatch", status=status.HTTP_400_BAD_REQUEST)  
            return Response(serializer.errors, status=status.HTTP_401_BAD_REQUEST)


class Logout(APIView):
    def get(self, request, format=None):
        request.session.flush()
        content = {'authentication' : 'User signout'}
        return Response(content, status=status.HTTP_200_OK)



class CreateProfile(APIView):

    @method_decorator(csrf_exempt)
    def get(self, request, format=None):
        content = ''
        response_status = 200
        if (request.session.get('username') == 'new_user' and request.session.get('login_method') == 'githuboauth'):
            response = create_userprofile_with_github_user_info(request)
            return response
        if (request.session.get('login_method') == 'manual'):
            content = 'Manual profile creation'
        return Response(content, status=response_status)

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

