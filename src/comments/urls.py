from django.urls import path

from comments.api import CommentsCreateAPI, CommentsListAPI

urlpatterns = [path("comments/create/", CommentsCreateAPI.as_view()), path("comments/", CommentsListAPI.as_view())]
