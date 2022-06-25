import json


class CRUDBase:
    def remove_ns1(self, obj: dict) -> dict:
        return json.loads(json.dumps(obj).replace('"ns1:', '"'))
