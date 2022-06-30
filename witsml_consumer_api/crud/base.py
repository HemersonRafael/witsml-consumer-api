# -*- coding: utf-8 -*-
"""Implementation of the base CRUD."""
import json


class CRUDBase:
    def clean_obj(self, obj: dict) -> dict:
        return json.loads(
            json.dumps(obj)
            .replace('"ns1:', '"')
            .replace('"@', '"')
            .replace(':ns1"', '"')
        )
