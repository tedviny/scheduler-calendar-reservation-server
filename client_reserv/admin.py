from django.contrib import admin
from client_reserv.models import Reservation, TimeSlot

# Register your models here.
admin.site.register(Reservation)
admin.site.register(TimeSlot)