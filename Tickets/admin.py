from django.contrib import admin
from Tickets.models import TicketsModel, User

# Register your models here.

admin.site.register(TicketsModel)
admin.site.register(User)

