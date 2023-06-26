from django.contrib import admin

# import models
from .models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ("name","countrycode", "district", "population")


admin.site.register(City,CityAdmin)
