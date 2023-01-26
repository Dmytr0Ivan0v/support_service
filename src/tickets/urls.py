from tickets.api import TicketAPISet
from django.urls import path


urlpatterns = [
    path("", TicketAPISet.as_view({"post": "create", "get": "list"})),
    path("<int:id_>/", TicketAPISet.as_view({"put": "update", "get": "retrieve"})),
    ]
