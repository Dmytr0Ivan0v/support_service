from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from shared.serialisers import ResponseMultiSerialiser, ResponseSerialiser
from users.permissions import IsSpecificUser, RoleIsAdmin
from users.serializers import UserCreateSerialiser, UserGetSerialiser

User = get_user_model()


class UserAPISet(ViewSet):
    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        elif self.action == "list":
            permission_classes = [RoleIsAdmin]
        elif self.action == "retrieve":
            permission_classes = [RoleIsAdmin | IsSpecificUser]
        elif self.action == "update":
            permission_classes = [IsSpecificUser]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserGetSerialiser(queryset, many=True)
        response = ResponseMultiSerialiser({"result": serializer.data})
        return JsonResponse(response.data)

    def retrieve(self, request, id_: int):
        instance = User.objects.get(id=id_)
        serializer = UserGetSerialiser(instance)
        self.check_object_permissions(request, instance)
        response = ResponseSerialiser({"result": serializer.data})
        return JsonResponse(response.data)

    def create(self, request):
        context = {"request": self.request}
        request.data["password"] = make_password(request.data["password"])
        serializer = UserCreateSerialiser(data=request.data, context=context)
        serializer.is_valid()
        serializer.save()
        response = ResponseSerialiser({"result": serializer.data})
        return JsonResponse(response.data)

    def update(self, request, id_: int):
        instance = User.objects.get(id=id_)
        context = {"request": self.request}
        serializer = UserGetSerialiser(instance, data=request.data, context=context)
        self.check_object_permissions(request, instance)
        serializer.is_valid()
        serializer.save()
        response = ResponseSerialiser({"result": serializer.data})
        return JsonResponse(response.data)
