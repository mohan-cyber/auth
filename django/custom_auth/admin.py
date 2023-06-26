from django.contrib import admin

# import models
from .models import CustomUser,OTPVerification

# custom user admin
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username","first_name", "last_name", "email", "gender", "phone")


class OTPVerificationAdmin(admin.ModelAdmin):
    list_display = ("user", "otp")
 

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(OTPVerification,OTPVerificationAdmin)
