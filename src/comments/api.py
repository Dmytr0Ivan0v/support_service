from typing import Any

from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView

from comments.serializers import CommentSerializer
from shared.serialisers import ResponseSerialiser
from tickets.models import Ticket
from users.constants import Role
from users.models import User


class CommentsCreateAPI(CreateAPIView):
    def user_validate(self, request, *args, **kwargs) -> bool:
        """
        Return 'True' for users who can create a comment to the specific
        ticket
        """
        ticket: Ticket = Ticket.objects.get(id=kwargs["ticket_id"])
        ticket_customer: User = ticket.customer
        ticket_manager: User | Any = ticket.manager

        return any([self.request.user == ticket_customer, self.request.user == ticket_manager])

    def add_fields(self, request):
        """
        Add necessary data to request acording to the 'Comment' model
        before calling '.is_valid()' inside 'crete' method
        """
        ticket_id = request.parser_context["kwargs"]["ticket_id"]
        ticket = Ticket.objects.get(id=ticket_id)
        last_comment = ticket.comments.last().id
        request.data["ticket"] = ticket_id
        request.data["user"] = request.user.id
        request.data["prev_comment"] = last_comment

    def create(self, request, *args, **kwargs):
        if self.user_validate(request, *args, **kwargs):
            context = {"request": self.request}
            self.add_fields(request)
            serializer = CommentSerializer(data=request.data, context=context)
            serializer.is_valid(raise_exception=True)
            response = ResponseSerialiser({"result": serializer.data})

            return JsonResponse(response.data, status=status.HTTP_201_CREATED)

        return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)


class CommentsListAPI(ListAPIView):
    serializer_class = CommentSerializer
    lookup_field = "ticket_id"
    lookup_url_kwarg = "ticket_id"

    def __get_tickets(self):
        role = self.request.user.role

        if role == Role.ADMIN:
            return Ticket.objects.all()
        if role == Role.MANAGER:
            return Ticket.objects.filter(manager=self.request.user)

        return Ticket.objects.filter(customer=self.request.user)

    def get_queryset(self) -> QuerySet:
        tickets = self.__get_tickets()
        ticket_id: int = self.kwargs[self.lookup_field]
        ticket: Ticket = get_object_or_404(tickets, id=ticket_id)
        comments = ticket.comments.order_by("-created_at")

        return comments

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return JsonResponse({"result": serializer.data})
