from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework import  serializers



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


    def login(self):
        username = self.validated_data['username']
        password = self.validated_data['password']

      
        user = auth.authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError({"detail": "No active account found with the given credentials."})
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username', 'email', 'password']
    
