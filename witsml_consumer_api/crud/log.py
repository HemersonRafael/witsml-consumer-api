# -*- coding: utf-8 -*-
"""Implementation of the log CRUD."""
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from komle import utils as ku
from komle.bindings.v1411.read import witsml
from komle.soap_client import StoreClient, StoreException
from pyxb.exceptions_ import PyXBException
from requests.exceptions import RequestException

from witsml_consumer_api.connecter import storage_client
from witsml_consumer_api.crud.base import CRUDBase
from witsml_consumer_api.exeptions import WitsmlConsumerApiError
from witsml_consumer_api.utils.utils import check_key, parser_log_curve_info


class CRUDLog(CRUDBase):
    def get(
        self,
        sc: StoreClient = storage_client,
        query_fields: dict = {'returnElements': 'id-only'},
    ) -> dict:
        query_fields = jsonable_encoder(query_fields, exclude_none=True)
        return_elements = query_fields['returnElements']
        xml_attribs = query_fields['xmlAttribs']
        options_in = query_fields['OptionsIn']
        del query_fields['returnElements']
        del query_fields['xmlAttribs']
        del query_fields['OptionsIn']
        try:
            logs_in_sc = self.clean_obj(
                ku.element_to_dict(
                    xml_attribs=xml_attribs,
                    element=sc.get_logs(
                        q_log=witsml.obj_log(**query_fields),
                        returnElements=return_elements,
                        OptionsIn=options_in,
                    ),
                )
            )
            if (
                return_elements == 'header-only' or return_elements == 'all'
            ) and xml_attribs == True:
                if 'log' in logs_in_sc['logs']:
                    if type(logs_in_sc['logs']['log']) is list:
                        logs_p = []
                        for log in logs_in_sc['logs']['log']:
                            log['startIndex'] = check_key(
                                check_key(log, 'startIndex'), '#text'
                            )
                            log['endIndex'] = check_key(
                                check_key(log, 'endIndex'), '#text'
                            )
                            log['logCurveInfo'] = parser_log_curve_info(
                                log['logCurveInfo']
                            )
                            logs_p.append(log)
                        logs_in_sc['logs']['log'] = logs_p
                    elif type(logs_in_sc['logs']['log']) is dict:
                        logs_in_sc['startIndex'] = check_key(
                            check_key(logs_in_sc, 'startIndex'), '#text'
                        )
                        logs_in_sc['endIndex'] = check_key(
                            check_key(logs_in_sc, 'endIndex'), '#text'
                        )
                        logs_in_sc['logs']['log'][
                            'logCurveInfo'
                        ] = parser_log_curve_info(
                            logs_in_sc['logs']['log']['logCurveInfo']
                        )

            return logs_in_sc

        except PyXBException as err:
            raise HTTPException(status_code=422, detail=str(err))
        except (RequestException, StoreException) as err:
            raise HTTPException(
                status_code=502,
                detail=f'{str(err)} or the query has a larger response than supported.',
            )
        except Exception as err:
            raise WitsmlConsumerApiError(str(err)) from err


log = CRUDLog()
