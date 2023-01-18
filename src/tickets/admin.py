from django.contrib import admin

from shared.django import TimeStampReadonlyAdmin
from tickets.models import Ticket


@admin.register(Ticket)
class TicketsAdmin(TimeStampReadonlyAdmin):
    list_display = ["header", "created_at", "updated_at"]
