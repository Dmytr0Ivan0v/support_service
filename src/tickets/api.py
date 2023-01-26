from functools import partial
from django.http import JsonResponse
from tickets.models import Ticket
from tickets.serializers import TicketLiteSerializer, TicketSerializer
from rest_framework.viewsets import ViewSet
from shared.serialisers import ResponseSerialiser, ResponseMultiSerialiser
from rest_framework import status


class TicketAPISet(ViewSet):
    
    def list(self, request):
        queryset = Ticket.objects.all()
        serializer = TicketLiteSerializer(queryset, many=True)
        for ticket in serializer.data:
            if len(ticket["body"]) > 100:
                ticket["body"] = f'{ticket["body"][:100]}...'
        response = ResponseMultiSerialiser({"result": serializer.data})
        return JsonResponse(response.data)

    def retrieve(self, request, id_: int):
        instance = Ticket.objects.get(id=id_)
        serializer = TicketSerializer(instance)
        response = ResponseSerialiser({"result": serializer.data})
        return JsonResponse(response.data)

    def create(self, request):
        context = {'request': self.request}
        serializer = TicketSerializer(data=request.data, context=context)
        serializer.is_valid()
        serializer.save()
        response = ResponseSerialiser({"result": serializer.data})
        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

    def update(self, request, id_: int):
        instance = Ticket.objects.get(id=id_)
        serializer = TicketSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid()
        serializer.save()
        response = ResponseSerialiser({"result": serializer.data})
        return JsonResponse(response.data)
