from django.core.mail import send_mail
from django.conf import settings
import uuid

def send_forgot_password(email,token):
     
    subject="your forgot the password"
    message=f"click on the link to reset the password http://127.0.0.1:8000/change_password/{token}/"
    email_from=settings.EMAIL.HOST.USER
    reception_list=[email]
    send_mail(subject,message,email_from,reception_list)
    return True