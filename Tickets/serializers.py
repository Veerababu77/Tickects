from Tickets.models import TicketsModel, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TicketsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = TicketsModel
        fields = ['ticket_title','ticket_status','ticket_mode','ticket_id','ticket_description','user']