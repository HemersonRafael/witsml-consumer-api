# -*- coding: utf-8 -*-
"""Create general-purpose utilities."""


def check_key(obj: dict | None, key: str):
    if obj is not None and key in obj:
        return obj[key]

    return None
