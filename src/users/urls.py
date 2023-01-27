from django.urls import path

from users.api import UserAPISet

urlpatterns = [
    path("", UserAPISet.as_view({"post": "create", "get": "list"})),
    path("<int:id_>/", UserAPISet.as_view({"put": "update", "get": "retrieve"})),
]
