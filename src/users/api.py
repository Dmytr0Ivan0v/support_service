from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from shared.serialisers import ResponseMultiSerialiser, ResponseSerialiser
from users.serializers import UserCreateSerialiser, UserGetSerialiser
from functools import partial
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ViewSet


User = get_user_model()


class UserAPISet(ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserGetSerialiser(queryset, many=True)
        response = ResponseMultiSerialiser({"result": serializer.data})
        return JsonResponse(response.data)

    def retrieve(self, request, id_: int):
        instance = User.objects.get(id=id_)
        serializer = UserGetSerialiser(instance)
        response = ResponseSerialiser({"result": serializer.data})
        return JsonResponse(response.data)

    def create(self, request):
        context = {'request': self.request}
        serializer = UserCreateSerialiser(data=request.data, context=context)
        serializer.is_valid()
        serializer.save()        
        response = ResponseSerialiser({"result": serializer.data})
        return JsonResponse(response.data)

    def update(self, request, id_: int):
        instance = User.objects.get(id=id_)
        serializer = UserGetSerialiser(instance, data=request.data, partial=partial)
        serializer.is_valid()
        serializer.save()
        response = ResponseSerialiser({"result": serializer.data})
        return JsonResponse(response.data)
