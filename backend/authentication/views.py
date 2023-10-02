from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import viewsets

# import serializers
from .serializers import LoginSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.login()
        token = RefreshToken.for_user(user)
        data = {
          "refresh": str(token),
          "access": str(token.access_token),
          "username":serializer.validated_data['username']
          
        }

        return Response(data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh = request.data["refresh"]
            print(refresh)
            token = RefreshToken(refresh)
            token.blacklist()
            return Response({"message": "Logged out successfully."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"message": "Logout operation failed."}, status=status.HTTP_400_BAD_REQUEST)










