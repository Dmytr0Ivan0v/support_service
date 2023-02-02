from functools import partial

from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ViewSet

from shared.serialisers import ResponseMultiSerialiser, ResponseSerialiser
from tickets.models import Ticket
from tickets.permissions import IsTicketManager, IsTicketOwner, RoleIsAdmin, RoleIsManager, RoleIsUser
from tickets.serializers import TicketLiteSerializer, TicketSerializer


class TicketAPISet(ViewSet):
    queryset = Ticket.objects.all()
    model = Ticket
    serializer_class = TicketSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [RoleIsUser]
        elif self.action == "list":
            permission_classes = [RoleIsAdmin | RoleIsManager]
        elif self.action == "retrieve":
            permission_classes = [IsTicketOwner | IsTicketManager | RoleIsAdmin]
        elif self.action == "update":
            permission_classes = [IsTicketManager | RoleIsAdmin]
        elif self.action == "delete":
            permission_classes = [IsTicketManager | RoleIsAdmin]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

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
        self.check_object_permissions(request, instance)
        response = ResponseSerialiser({"result": serializer.data})

        return JsonResponse(response.data)

    def create(self, request):
        context = {"request": self.request}
        serializer = TicketSerializer(data=request.data, context=context)
        serializer.is_valid()
        serializer.save()
        response = ResponseSerialiser({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

    def update(self, request, id_: int):
        instance = Ticket.objects.get(id=id_)
        serializer = TicketSerializer(instance, data=request.data, partial=partial)
        self.check_object_permissions(request, instance)
        serializer.is_valid()
        serializer.save()
        response = ResponseSerialiser({"result": serializer.data})

        return JsonResponse(response.data)

    def delete(self, request, id_: int):
        instance = Ticket.objects.get(id=id_)
        self.check_object_permissions(request, instance)
        instance.delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
