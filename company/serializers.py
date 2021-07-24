from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255,min_length=4,write_only=True)
    email = serializers.EmailField(max_length=255,min_length=4)
    class Meta:
       model = User
       fields = ['id','username','email','password']

    def validate(self,attrs):
        email = attrs.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('Email is already exists')})
        return super().validate(attrs)

    def create(self,validate_data):
        return User.objects.create_user(**validate_data)


