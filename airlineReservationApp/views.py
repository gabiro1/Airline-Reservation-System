from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket, Airport, Flight, Payment
from django.utils import timezone
from datetime import timedelta
from .serializers import AirportSerializer, FlightSerializer, TicketSerializer, PaymentSerializer


class AirportList(APIView):
    def get(self, request):
        """Handle GET requests to retrieve all airports."""
        airports = Airport.objects.all()
        serializer = AirportSerializer(airports, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Handle POST requests to create a new airport."""
        serializer = AirportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlightList(APIView):
    def get(self, request):
        """Handle GET requests to retrieve all flights."""
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Handle POST requests to create a new flight."""
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketList(APIView):
    def get(self, request):
        """Handle GET requests to retrieve all tickets."""
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Handle POST requests to create a new ticket."""
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketCancel(APIView):
    def post(self, request, ticket_id):
        """Handle POST requests to cancel a ticket."""
        try:
            ticket = Ticket.objects.get(id=ticket_id)

            # Check if the ticket is already canceled
            if ticket.status == 'canceled':
                return Response({'error': 'Ticket has already been canceled.'}, status=status.HTTP_400_BAD_REQUEST)

            # Check cancellation time restrictions (e.g., 24 hours before the flight)
            if ticket.flight.departure_time - timezone.now() < timedelta(hours=24):
                return Response({'error': 'Cannot cancel ticket within 24 hours of the flight.'}, status=status.HTTP_400_BAD_REQUEST)

            # Update ticket status
            ticket.status = 'canceled'
            ticket.save()

            # Optionally process refund here

            return Response({'message': 'Ticket canceled successfully.'}, status=status.HTTP_200_OK)

        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PaymentList(APIView):
    def get(self, request):
        """Handle GET requests to retrieve all payments."""
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Handle POST requests to create a new payment."""
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentProcess(APIView):
    def post(self, request, ticket_id):
        """Handle POST requests to process payment for a ticket."""
        try:
            # Retrieve the ticket using the provided ticket_id
            ticket = Ticket.objects.get(id=ticket_id)

            # The amount to be charged (this could depend on ticket details)
            amount = ticket.price  # Assuming 'price' is an attribute of your Ticket model

            # Simulating payment processing logic
            payment_data = {
                'ticket': ticket,
                'amount': amount,
                'status': 'pending',  # Initial status
            }

            # Normally, you would call an external payment API here
            # For this example, we'll simulate a successful payment
            payment_successful = True  # Simulating payment success

            if payment_successful:
                # Update status if payment is successful
                payment_data['status'] = 'completed'
                payment = Payment(**payment_data)
                payment.save()  # Save payment record in the database

                # Return success response
                return Response({'message': 'Payment processed successfully.', 'payment_id': payment.id}, status=status.HTTP_201_CREATED)
            else:
                # Handle payment failure
                return Response({'error': 'Payment processing failed.'}, status=status.HTTP_400_BAD_REQUEST)

        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)