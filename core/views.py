from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer, ChangePasswordSerializer, UserProfileSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView



class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user = User.objects.get(email=user.email)
            # try:
            #     pfob = Profile.objects.get(user=user)
            #     pfob.save()
            # except Profile.DoesNotExist:
            #     pass

            email = user.email
            id = user.id
            token = RefreshToken.for_user(user)
            token["email"] = user.email
            data = {
                "id": id,
                "email": email,
                "access_token": str(token.access_token),
                "refresh_token": str(token),
            }
            return Response({"data": data, "msg": "registration successful"}, status=status.HTTP_201_CREATED)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({"msg": "password changed successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProfileSettingView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            user_obj = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            return Response({"error": "User is Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(user_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        try:
            user_obj = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"error": "User is Not found"}, status=status.HTTP_404_NOT_FOUND)
        if user_obj == request.user:
            serializer = UserProfileSerializer(user_obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "not autherized"}, status=status.HTTP_403_FORBIDDEN)
        
    def put(self, request, pk):
        try:
            user_obj = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"error": "User is Not found"}, status=status.HTTP_404_NOT_FOUND)
        if user_obj == request.user:
            serializer = UserProfileSerializer(user_obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "not autherized"}, status=status.HTTP_403_FORBIDDEN)
        
    def patch(self, request, pk):
        try:
            user_obj = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"error": "User is Not found"}, status=status.HTTP_404_NOT_FOUND)
        if user_obj == request.user:
            serializer = UserProfileSerializer(user_obj, data=request.data, partial = True)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "not autherized"}, status=status.HTTP_403_FORBIDDEN)