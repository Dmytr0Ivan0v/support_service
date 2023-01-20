from rest_framework import serializers

from tickets.models import Ticket


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["header", "body"]


class TicketLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        # exclude = ["body"]


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
