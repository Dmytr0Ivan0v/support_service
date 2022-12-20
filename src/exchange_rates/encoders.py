import json
from decimal import Decimal


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
