from django.urls import path
from Tickets.views import TicketsGetAPI, UserTicketsGetAPI, filteringGetAPI

urlpatterns = [
    path('tickets/',TicketsGetAPI.as_view()),
    path('tickets/user/<int:id>/',UserTicketsGetAPI.as_view()),
    path('tickets/filter/<str:ticket_mode>/', filteringGetAPI.as_view()),
]
