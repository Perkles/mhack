import requests, json

from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


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
        # Callback function to https://github.com/login/oauth/authorize?client_id=dc885fbf11d3232616bc
        # if the user log in successfully in Github the callback should return a query param named
        # code.
        code_response = self.request.query_params.get('code')


        response = requests.post("https://github.com/login/oauth/access_token", data = {
            'client_id': 'dc885fbf11d3232616bc',
            'client_secret': 'a9d70f98b5bd165cbe45f9b767a9869e25792587',
            'code': code_response
        })
    
        print(response.text)
        response_json = response.json()
        print(response_json)

        if response:
            return Response(status=status.HTTP_201_CREATED)


    # https://github.com/login/oauth/authorize?client_id=dc885fbf11d3232616bc
    #     const code = req.query.code;
    # console.log(code);

    # // request.js post request npm run dev
    # const options = {
    #     url: 'https://github.com/login/oauth/access_token',
    #     json: true,
    #     body: {
    #         client_id: 'dc885fbf11d3232616bc',
    #         client_secret: 'a9d70f98b5bd165cbe45f9b767a9869e25792587',
    #         code: code
    #     }
    # };
    
    # request.post(options, (err, res, body) => {
    #     if (err) {
    #         return console.log(err);
    #     }
    #     console.log(`Status: ${res.statusCode}`);
    #     console.log(body);
    # });



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

