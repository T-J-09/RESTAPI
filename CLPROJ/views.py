from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

class clientapi(APIView):
    permission_classes = (AllowAny,)

    def post(self,request,format=None):
        data = request.data
        cl_data={'created_by':1}
        data.update(cl_data)
        serialzerr = ClientCretSerializer(data=data)
        if serialzerr.is_valid():
            serialzerr.save()
            client_data = Clients.objects.get(id=serialzerr.data['id']) #fetch by id
            clientsserializer = ClientsSerializer(client_data).data
            return Response(clientsserializer, status=status.HTTP_201_CREATED)
        else:
            return Response(serialzerr.errors,status=status.HTTP_201_CREATED)

    def get(self,request,format=None):
        client_data= Clients.objects.filter().order_by('-created_at')
        clientsserializer = ClientsSerializer(client_data,many=True).data
        return Response(clientsserializer,status=status.HTTP_201_CREATED)


class clientdtl(APIView):
    permission_classes = (AllowAny,)
    def delete(self, request,pk, format=None):
        Clients.objects.filter(id=pk).delete()
        return Response({'message': 'Record is deleted successfully!!'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request,pk,format=None):
        data=request.data
        Clients.objects.filter(id=pk).update(**data)
        client_data= Clients.objects.get(id=pk)
        clientsserializer = ClientsSerializer(client_data).data
        return Response(clientsserializer,status=status.HTTP_201_CREATED)

class projapi(APIView):
    permission_classes = (AllowAny,)

    def post(self,request,format=None):
        data = request.data
        serialzerr=  ProjCreateSeralizer(data=data)
        if serialzerr.is_valid():
            serialzerr.save()
            return Response('New Project Created',status=status.HTTP_201_CREATED)
        else:
            return Response(serialzerr.errors,status=status.HTTP_201_CREATED)

    def get(self,request,format=None):
        proj_data = projects.objects.filter().order_by('-created_at')#order by desc
        projserializer = ProjSeralizer(proj_data,many=True).data
        return Response(projserializer,status=status.HTTP_201_CREATED)

