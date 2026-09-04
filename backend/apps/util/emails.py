from django.core.mail import send_mail


def send_otp_email(email, otp):
    send_mail(
        subject="One Time Password for SignUp.",
        message=f"Your One Time Password for DineCare is {otp}",
        from_email="noreply@example.com",
        recipient_list=[email]
    )
