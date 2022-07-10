# -*- coding: utf-8 -*-
"""Implementation of the base CRUD."""
import ujson


class CRUDBase:
    def clean_obj(self, obj: dict) -> dict:
        return ujson.loads(
            ujson.dumps(obj)
            .replace('"ns1:', '"')
            .replace('"@', '"')
            .replace(':ns1"', '"')
        )
