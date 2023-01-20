from django.http import JsonResponse
from django.urls import path
from rest_framework.generics import CreateAPIView, ListAPIView

from tickets.models import Ticket
from tickets.serializers import TicketLiteSerializer, TicketSerializer


class TicketsGet(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketLiteSerializer

    def dispatch(self, request, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs
        request = self.initialize_request(request, *args, **kwargs)
        self.request = request
        self.headers = self.default_response_headers

        try:
            self.initial(request, *args, **kwargs)

            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed

            response = handler(request, *args, **kwargs)

        except Exception as exc:
            response = self.handle_exception(exc)

        self.response = self.finalize_response(request, response, *args, **kwargs)

        for el in response.data:
            if len(el["body"]) > 100:
                el["body"] = f'{el["body"][:100]}...'

        return self.response


def get_ticket(requesr, id_: int) -> JsonResponse:
    ticket: Ticket = Ticket.objects.get(id=id_)
    serializer = TicketSerializer(ticket)

    return JsonResponse(serializer.data)


class TicketCreateApi(CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


urlpatterns = [
    path("list/", TicketsGet.as_view()),
    path("create/", TicketCreateApi.as_view()),
    path("<int:id_>/", get_ticket),
]
