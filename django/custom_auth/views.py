from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout 
import random 

# models
from .models import CustomUser , OTPVerification

# serializers
from .serializers import CustomUserSerializer, LoginSerializer 

from mail.utils import Utils

class SignupView(APIView):
    signup_serializer_class = CustomUserSerializer
    
    def post(self, request):
        signup_serializer = self.signup_serializer_class(data=request.data)
        signup_serializer.is_valid(raise_exception=True)
        signup_serializer.save()

        return Response({"message": "User registration completed successfully."}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    login_serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.login_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        entered_otp = serializer.validated_data['otp']

        try:
            user = CustomUser.objects.get(email=email)
            print(user.username)
        except CustomUser.DoesNotExist:
            return Response({"error": "User doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        otp, created = OTPVerification.objects.get_or_create(user=user)
        
        if created:
            verification_otp = random.randint(1000, 9999)
            Utils.send_otp_email(user.email, verification_otp)
            otp.otp = verification_otp
            otp.save()

            return Response({"message": "OTP has been successfully sent to your email"},
                            status=status.HTTP_200_OK)

        if str(entered_otp) == str(otp.otp):
            otp.delete()
            # user = CustomUser.objects.get(email=email)
            # user = auth.authenticate(request, username="mohan")
            if user is not None:
                login(request, user)
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Failed to authenticate user"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error": "Incorrect OTP"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
