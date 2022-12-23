import json
from decimal import Decimal

from django.http import JsonResponse


class ForDecimalJSONEncoder(json.JSONEncoder):
    """
    JSONEncoder subclass that knows how to encode decimal type to digital view.
    """

    def default(self, o):
        if isinstance(o, Decimal):
            r = float(o)
            return r
        else:
            return super().default(o)


class ForDecimalJsonResponse(JsonResponse):
    def __init__(self, data, **kwargs):
        JsonResponse.__init__(
            self,
            data,
            encoder=ForDecimalJSONEncoder,
            safe=True,
            json_dumps_params=None,
            **kwargs
        )
