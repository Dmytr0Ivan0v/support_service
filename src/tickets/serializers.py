from rest_framework import serializers

from tickets.models import Ticket



class TicketLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
   
    class Meta:
        model = Ticket
        fields = ["id", "header", "body", "customer"]
