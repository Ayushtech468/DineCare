import random
from django.core.mail import send_mail
from django.core.cache import cache

def generate_otp():
    return str(random.randint(100000, 999999))


def store_otp(email, otp):

    cache.set(
        f"otp_{email}",
        otp,
        timeout=300
    )


def verify_stored_otp(email, otp):
    stored_otp = cache.get(f"otp_{email}")

    if not stored_otp:
        return False
    
    return stored_otp == str(otp)


def delete_otp(email):
    cache.delete(f"otp_{email}")