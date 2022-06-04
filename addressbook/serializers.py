from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def validate_latitude(self, value):
        if (value>(-90) and value<90):
            return value
        else:
            return serializers.ValidationError('Invalid latitude')
    
    def validate_longitude(self, value):
        if (value>(-180) and value<180):
            return value
        else:
            return serializers.ValidationError('Invalid longitude')
