from django.contrib import admin
from .models import Airport,Ticket,Payment,Flight

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Payment)