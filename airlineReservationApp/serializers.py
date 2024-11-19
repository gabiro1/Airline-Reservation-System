from rest_framework import serializers
from .models import Airport, Flight, Ticket, Payment

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model: Airport
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model= Flight
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
    
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'