from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=30, unique=True)
    city = models.CharField(max_length=255)
    country = models. CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Flight(models.Model):
    flight_number = models.CharField(max_length=200, unique=True)
    airline = models.CharField(max_length=100)
    departure_airport = models.ForeignKey(Airport,related_name='departures',on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport,related_name='arrivals',on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.DurationField()
    total_seats = models.IntegerField()
    available = models.IntegerField()


class Ticket(models.Model):
    TICKET_STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('canceled', 'Canceled'),
    ]
    
    ticket_number = models.CharField(max_length=20)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=TICKET_STATUS_CHOICES, default='booked')

    def __str__(self):
        return self.ticket_number

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15,decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=20, choices=[('successful','successful'),('Failed','Failed')])

