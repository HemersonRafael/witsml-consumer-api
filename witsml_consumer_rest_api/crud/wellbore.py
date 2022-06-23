from typing import List

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from komle import utils as ku
from komle.bindings.v1411.read import witsml
from komle.soap_client import StoreClient, StoreException
from pyxb.exceptions_ import PyXBException
from requests.exceptions import RequestException

from witsml_consumer_rest_api.connecter import store_client
from witsml_consumer_rest_api.exeptions import WitsmlConsumerApiError
from witsml_consumer_rest_api.utils.utils import check_key


class CRUDWellbore:
    def get(
        self,
        sc: StoreClient = store_client,
        query_fields: dict = {'returnElements': 'header-only'},
    ) -> List[dict] | dict:
        query_fields = jsonable_encoder(query_fields, exclude_none=True)
        return_elements = query_fields['returnElements']
        del query_fields['returnElements']
        try:
            return check_key(
                check_key(
                    ku.element_to_dict(
                        sc.get_wellbores(
                            witsml.obj_wellbore(**query_fields),
                            returnElements=return_elements,
                        )
                    ),
                    'ns1:wellbores',
                ),
                'ns1:wellbore',
            )
        except PyXBException as err:
            raise HTTPException(status_code=422, detail=str(err))
        except (RequestException, StoreException) as err:
            raise HTTPException(status_code=502, detail=str(err))
        except Exception as err:
            raise WitsmlConsumerApiError(str(err)) from err


wellbore = CRUDWellbore()
