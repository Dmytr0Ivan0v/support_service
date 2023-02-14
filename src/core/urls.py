from django.urls import include, path

urlpatterns = [
    path("tickets/", include("tickets.urls")),
    path("tickets/<int:ticket_id>/", include("comments.urls")),
]
