import json

from django.http import JsonResponse

from exchange_rates.domain import (ExchangeRatesServiceRequest,
                                   ExchangeRatesServiceResponse)
from exchange_rates.encoders import ForDecimalJsonResponse
from exchange_rates.services import ExchangeRatesService


def convert(request) -> JsonResponse:
    if request.method == "POST":
        data: dict = json.loads(request.body)
        from_currency: str = data["from"]
        to_currency: str = data["to"]
        exchange_rates_service = ExchangeRatesService(
            request=ExchangeRatesServiceRequest(
                from_currency=from_currency, to_currency=to_currency
            )
        )
        result: ExchangeRatesServiceResponse = exchange_rates_service.convert()
        return ForDecimalJsonResponse(result.dict())
    else:
        response = {"invalid request method": "not 'POST'"}
        return JsonResponse(response)
