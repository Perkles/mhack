import requests, json

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from authentication.models import User, Profile
from authentication.serializer import UserSerlializer, ProfileSerializer
from githubapi.authenticate import Authenticate

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

class Logout(APIView):
    def get(self, request, format=None):
        request.session.flush()
        content = {'authentication' : 'User signout'}
        return Response(content, status=status.HTTP_200_OK)

        
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

