from django.urls import path# include is used to include app URLs

from airlineReservationApp.views import FlightList, AirportList, TicketList, PaymentList, TicketCancel


class PaymentProcess:
    @classmethod
    def as_view(cls):
        pass


urlpatterns = [

    path('airports/', AirportList.as_view(), name='airport_list'),
    path('flights/', FlightList.as_view(), name='flight_list'),
    path('tickets/', TicketList.as_view(), name='ticket_list'),
    #  path('tickets/cancel/<int:ticket_id>/', TicketCancel.as_view(), name='ticket_cancel'),  # Cancel a ticket
    # path('tickets/<int:ticket_id>/payment/', PaymentProcess.as_view(), name='payment_process'),
      # Include app URLs under the 'api/' path
]
