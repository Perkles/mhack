from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from tutorial.models import Test
from tutorial.serializer import TestSerializer

class Test_list(APIView):

    def get(self, request, format=None):
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Test_detail(APIView):

    def get_object(self, pk):
        try:
            return Test.objects.get(pk=pk)
        except Test.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = TestSerializer(test)
        return Response(serializer.data)

    @method_decorator(csrf_exempt)
    def put(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @method_decorator(csrf_exempt)
    def delete(self, request, pk, format=None):
        test = self.get_object(pk)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

