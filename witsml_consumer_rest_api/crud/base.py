# -*- coding: utf-8 -*-
"""Implementation of the base CRUD."""
import json


class CRUDBase:
    def remove_ns1(self, obj: dict) -> dict:
        return json.loads(json.dumps(obj).replace('"ns1:', '"'))
