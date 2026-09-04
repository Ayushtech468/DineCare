from rest_framework import serializers


class SendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15, required=False)
    otp = serializers.CharField(min_length=6, max_length=6)
