# -*- coding: utf-8 -*-
"""Implementation of the log CRUD."""
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from komle import utils as ku
from komle.bindings.v1411.api import cap_server
from komle.bindings.v1411.read import witsml
from komle.soap_client import StoreClient, StoreException
from pyxb.exceptions_ import PyXBException
from requests.exceptions import RequestException

from witsml_consumer_api.connecter import storage_client
from witsml_consumer_api.crud.base import CRUDBase
from witsml_consumer_api.exeptions import WitsmlConsumerApiError
from witsml_consumer_api.utils.utils import check_key, parser_log_curve_info


class CRUDCapability(CRUDBase):
    def get(self, sc: StoreClient = storage_client):
        try:
            return self.clean_obj(
                ku.element_to_dict(
                    xml_attribs=True, element=sc.get_cap(dataVersion='1.4.1.1')
                )
            )
        except PyXBException as err:
            raise HTTPException(status_code=422, detail=str(err))
        except (RequestException, StoreException) as err:
            raise HTTPException(
                status_code=502,
                detail=f'{str(err)}',
            )
        except Exception as err:
            raise WitsmlConsumerApiError(str(err)) from err


capability = CRUDCapability()
