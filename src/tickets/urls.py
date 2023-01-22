from django.http import JsonResponse
from django.urls import path
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from tickets.models import Ticket
from tickets.serializers import TicketLiteSerializer, TicketSerializer


class TicketsGet(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketLiteSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        for ticket in serializer.data:
            if len(ticket["body"]) > 100:
                ticket["body"] = f'{ticket["body"][:100]}...'
        return Response(serializer.data)


def get_ticket(requesr, id_: int) -> JsonResponse:
    ticket: Ticket = Ticket.objects.get(id=id_)
    serializer = TicketSerializer(ticket)

    return JsonResponse(serializer.data)


class TicketCreateApi(CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


urlpatterns = [
    path("list/", TicketsGet.as_view()),
    path("create/", TicketCreateApi.as_view()),
    path("<int:id_>/", get_ticket),
]
