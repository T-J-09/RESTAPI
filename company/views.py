from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from . serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.decorators import api_view


class RegView(GenericAPIView):
     serializer_class = UserSerializer

     def post(self,request):
          serializer = UserSerializer(data=request.data)

          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data ,status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


     def get(request):
          if request.method == 'GET':
               api = UserSerializer.objects.get()
               slizer = UserSerializer(api, many =True)
               return JsonResponse(slizer.data)




