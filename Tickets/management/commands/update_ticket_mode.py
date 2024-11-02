from celery import shared_task
from django.utils import timezone
from Tickets.models import TicketsModel
from datetime import timedelta

@shared_task
def update_ticket_modes():
    now = timezone.now()
    two_days_ago = now - timedelta(days=2)
    five_days_ago = now - timedelta(days=5)

    TicketsModel.objects.filter(created__lte=two_days_ago).update(ticket_mode='medium')
    TicketsModel.objects.filter(created__lte=five_days_ago).update(ticket_mode='urgent')
