from django.http import JsonResponse
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from tickets.models import Ticket
from tickets.serializers import TicketCreateSerializer, TicketLiteSerializer, TicketSerializer


class TicketsGet(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketLiteSerializer


def get_ticket(requesr, id_: int) -> JsonResponse:
    ticket: Ticket = Ticket.objects.get(id=id_)
    serializer = TicketSerializer(ticket)

    return JsonResponse(serializer.data)


@api_view(["POST"])
def create_ticket(request) -> JsonResponse:
    serializer = TicketCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    Ticket.objects.create(**serializer.validated_data)

    return JsonResponse(serializer.validated_data)


urlpatterns = [path("/", TicketsGet.as_view()), path("/<int:id_>", get_ticket), path("/create", create_ticket)]
