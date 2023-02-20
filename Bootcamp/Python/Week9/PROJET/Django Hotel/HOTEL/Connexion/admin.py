
from django.contrib import admin
from Connexion.models import Customer, RoomManager
from Reservation.models import Contact,Rooms,Booking
# Register your models here.
admin.site.register(Customer)
admin.site.register(RoomManager)
admin.site.register(Contact)
admin.site.register(Rooms)
admin.site.register(Booking)