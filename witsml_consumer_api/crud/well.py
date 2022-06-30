# -*- coding: utf-8 -*-
"""Implementation of the well CRUD."""
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


class CRUDWell(CRUDBase):
    def get(
        self,
        sc: StoreClient = storage_client,
        query_fields: dict = {'returnElements': 'all'},
    ) -> dict:
        query_fields = jsonable_encoder(query_fields, exclude_none=True)
        return_elements = query_fields['returnElements']
        xml_attribs = query_fields['xmlAttribs']
        options_in = query_fields['OptionsIn']
        del query_fields['returnElements']
        del query_fields['xmlAttribs']
        del query_fields['OptionsIn']
        try:
            return self.clean_obj(
                ku.element_to_dict(
                    xml_attribs=xml_attribs,
                    element=sc.get_wells(
                        q_well=witsml.obj_well(**query_fields),
                        returnElements=return_elements,
                        OptionsIn=options_in,
                    ),
                )
            )
        except PyXBException as err:
            raise HTTPException(status_code=422, detail=str(err))
        except (RequestException, StoreException) as err:
            raise HTTPException(status_code=502, detail=str(err))
        except Exception as err:
            raise WitsmlConsumerApiError(str(err)) from err


well = CRUDWell()
