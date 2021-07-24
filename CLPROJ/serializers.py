from .models import *
from rest_framework import serializers

class ProjClSeralizer(serializers.ModelSerializer):

    class Meta:
        model = projects
        fields = ['id','project_name']

class ClientsSerializer(serializers.ModelSerializer):
    created_by=serializers.SlugRelatedField(read_only=True, slug_field='username')
    project = ProjClSeralizer(many=True)
    class Meta:
        model = Clients
        fields = '__all__'

class ClientCretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
        def create(self, validated_data):
            return Clients.objects.create(**validated_data)

class ProjSeralizer(serializers.ModelSerializer):
    users = serializers.SlugRelatedField(many=True,read_only=True, slug_field='username') #foergin key related
    created_by = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = projects
        fields = '__all__'

class ProjCreateSeralizer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = '__all__'

        def create(self,validate_data):
            return projects.objects.create(**validate_data)

