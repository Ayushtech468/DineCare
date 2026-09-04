from apps.user.serializers import SendOTPSerializer, VerifyOTPSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.models import User

from apps.user.utils import (
    generate_otp,
    store_otp,
    verify_stored_otp,
    delete_otp,
)
from apps.util.emails import send_otp_email


class SendOTPView(APIView):
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']

        otp = generate_otp()

        store_otp(email, otp)

        send_otp_email(email, otp)

        return Response(
            {
                "message": "OTP sent successfully!",
            },
            status=status.HTTP_200_OK
        )


class VerfiyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        phone_number = serializer.validated_data['phone_number']
        otp = serializer.validated_data['otp']

        valid_otp = verify_stored_otp(email, otp)

        if not valid_otp:
            return Response(
                {
                    "error": "Invalid or Expired OTP."
                }
            )

        delete_otp(email)

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "phone_number": phone_number
            })

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "message": (
                    "User registered successfully."
                    if created
                    else
                    "Login successfully."
                ),
                "access_token": str(refresh.access_token),
                "refresh": str(refresh)
            }
        )
