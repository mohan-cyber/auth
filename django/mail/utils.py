from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


class Utils:
    @staticmethod
    def send_otp_email(email, otp):
        subject = 'OTP Verification'
        html_message = render_to_string('otp_email.html', {'otp': otp})
        plain_message = strip_tags(html_message)
        from_email = 'mohanaselvan014@gmail.com'  
        recipient_list = [email]

        send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)