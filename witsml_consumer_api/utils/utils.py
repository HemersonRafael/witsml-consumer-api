# -*- coding: utf-8 -*-
"""Create general-purpose utilities."""


def check_key(obj: dict | None, key: str):
    if obj is not None and key in obj:
        return obj[key]

    return None


def parser_log_curve_info(
    log_curves_info: list[dict],
) -> list[dict]:
    if type(log_curves_info) is dict:
        log_curve_info['minIndex'] = check_key(
            check_key(log_curve_info, 'minIndex'), '#text'
        )
        log_curve_info['maxIndex'] = check_key(
            check_key(log_curve_info, 'maxIndex'), '#text'
        )
        lci = log_curve_info
    elif type(log_curves_info) is list:
        lci = []
        for log_curve_info in log_curves_info:
            log_curve_info['minIndex'] = check_key(
                check_key(log_curve_info, 'minIndex'), '#text'
            )
            log_curve_info['maxIndex'] = check_key(
                check_key(log_curve_info, 'maxIndex'), '#text'
            )

            lci.append(log_curve_info)
    else:
        lci = log_curve_info

    return lci
