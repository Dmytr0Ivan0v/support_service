from django.urls import path

from tickets.api import TicketAPISet

urlpatterns = [
    path("", TicketAPISet.as_view({"post": "create", "get": "list"})),
    path("<int:id_>/", TicketAPISet.as_view({"put": "update", "get": "retrieve", "delete": "delete"})),
]
