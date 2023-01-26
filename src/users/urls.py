from users.api import UserAPISet
from django.urls import path


urlpatterns = [
    path("", UserAPISet.as_view({"post": "create", "get": "list"})),
    path("<int:id_>/", UserAPISet.as_view({"put": "update", "get": "retrieve"})),
]
