from rest_framework import serializers

# import models
from .models import City

# Country serializer
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'countrycode', 'district', 'population']

