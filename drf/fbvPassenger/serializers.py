from rest_framework import serializers
from fbvPassenger.models import Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields='__all__'
