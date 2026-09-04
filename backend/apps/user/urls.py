from django.urls import path
from apps.user.views import SendOTPView, VerfiyOTPView


urlpatterns = [
    path('send-otp/', SendOTPView.as_view(), name='send-otp'),
    path('verify-otp/', VerfiyOTPView.as_view(), name="verify-otp")
]
