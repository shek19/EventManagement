# users/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
# from rest_framework.decorators import api_view,permission_classes

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "message": "User created successfully",
        }, status=status.HTTP_201_CREATED)






# # users/views.py
# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# from .serializers import RegisterSerializer, LoginSerializer
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             "user": serializer.data,
#             "token": token.key
#         }, status=status.HTTP_201_CREATED)

# class LoginView(APIView):
#     serializer_class = LoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         username = serializer.validated_data['username']
#         password = serializer.validated_data['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
