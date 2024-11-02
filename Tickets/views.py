from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from Tickets.models import User, TicketsModel
from Tickets.serializers import UserSerializer, TicketsSerializer
from django.utils import timezone
from datetime import timedelta


class TicketsGetAPI(APIView):
    def get(self, request):
        queryset = TicketsModel.objects.all()
        all_tickets = TicketsModel.objects.all().count()
        # print(all_tickets)
        open_tickets = TicketsModel.objects.filter(ticket_status = 'open').count()
        close_tickets = TicketsModel.objects.filter(ticket_status = 'close').count()
        in_progress_tickets = all_tickets-(open_tickets+close_tickets)
        
        serializer = TicketsSerializer(queryset,many = True)
        return Response(
                        {
                            'all_tickets_data':serializer.data,
                            'total_tickets':all_tickets,
                            'open_tickets': open_tickets,
                            'close_tickets': close_tickets,
                            'in_progress_tickets': in_progress_tickets
                        }
                        )
    
    # def put(self, request):
    #     new_date = timezone.now() - timedelta(days = 2)
    #     new_date1 = timezone.now() - timedelta(days = 5)
        
    #     ticket = TicketsModel.objects.filter(created__lte = new_date1)
    #     tickets = TicketsModel.objects.filter(created__lte = new_date)
    #     if not tickets.exists():
    #         return Response({"message": "No tickets found that were created two days ago."}, status=status.HTTP_404_NOT_FOUND)
    #     if not ticket.exists():
    #         return Response({"message": "No tickets found that were created five days ago."}, status=status.HTTP_404_NOT_FOUND)
        
    #     tickets.update(ticket_mode='medium')
    #     ticket.update(ticket_mode = 'urgent')
    #     return Response({
    #         'messege':'updated successfully'
    #     })
        
        
    
class UserTicketsGetAPI(APIView):
    def get(self,request, id):
        try:
            user = User.objects.get(pk=id)
            print(user)
        except:
            return Response({'messege':'Not'})
        tickets = TicketsModel.objects.filter(user = user)
        print(tickets)
        serializer = TicketsSerializer(tickets, many = True)
        print(serializer)
        return Response(serializer.data)
    
    def put(self, request, id):
        try:
            queryset = TicketsModel.objects.get(pk = id)
        except:
            return Response({'messege': 'bad request'})
        new_status = request.data.get('ticket_status')
        queryset.ticket_status = new_status
        queryset.save()
        serializer = TicketsSerializer(queryset)
        return Response(serializer.data)
    
class filteringGetAPI(APIView):
    def get(self, request, ticket_mode):
        tickets = TicketsModel.objects.filter(ticket_mode = ticket_mode).exclude(ticket_status = 'close')
        if not tickets.exists():
            return Response({'messege':'No tickets are available'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TicketsSerializer(tickets, many = True)
        return Response(serializer.data)
        
        
