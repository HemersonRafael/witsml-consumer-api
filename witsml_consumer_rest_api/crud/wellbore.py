# -*- coding: utf-8 -*-
"""Implementation of the wellbore CRUD."""
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from komle import utils as ku
from komle.bindings.v1411.read import witsml
from komle.soap_client import StoreClient, StoreException
from pyxb.exceptions_ import PyXBException
from requests.exceptions import RequestException

from witsml_consumer_rest_api.connecter import storage_client
from witsml_consumer_rest_api.crud.base import CRUDBase
from witsml_consumer_rest_api.exeptions import WitsmlConsumerApiError


class CRUDWellbore(CRUDBase):
    def get(
        self,
        sc: StoreClient = storage_client,
        query_fields: dict = {'returnElements': 'header-only'},
    ) -> dict:
        query_fields = jsonable_encoder(query_fields, exclude_none=True)
        return_elements = query_fields['returnElements']
        del query_fields['returnElements']
        try:
            return self.remove_ns1(
                ku.element_to_dict(
                    sc.get_wellbores(
                        witsml.obj_wellbore(**query_fields),
                        returnElements=return_elements,
                    )
                )
            )
        except PyXBException as err:
            raise HTTPException(status_code=422, detail=str(err))
        except (RequestException, StoreException) as err:
            raise HTTPException(status_code=502, detail=str(err))
        except Exception as err:
            raise WitsmlConsumerApiError(str(err)) from err


wellbore = CRUDWellbore()
