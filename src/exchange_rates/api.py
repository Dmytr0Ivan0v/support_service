import json

import requests
from django.conf import settings
from django.http import JsonResponse

from exchange_rates import encoders, services


def convert(request) -> JsonResponse:
    if request.method == "POST":
        data: dict = json.loads(request.body)
        from_currency: str = data["from"]
        to_currency: str = data["to"]
        url = (
            f"{settings.ALPHA_VANTAGE_BASE_URL}/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&"
            f"to_currency={to_currency}&apikey={settings.ALPHA_VANTAGE_API_KEY}"
        )
        response = requests.get(url)
        alphavantage_response = services.AlphavantageResponse(**response.json())
        return JsonResponse(
            alphavantage_response.results.dict(), encoder=encoders.ForDecimalJSONEncoder
        )
    else:
        response = {"invalid request method": "not 'POST'"}
        return JsonResponse(response)
