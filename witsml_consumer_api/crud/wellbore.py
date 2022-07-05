# -*- coding: utf-8 -*-
"""Implementation of the wellbore CRUD."""
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
from witsml_consumer_api.utils.utils import check_key


class CRUDWellbore(CRUDBase):
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
            wellbores_in_sc = self.clean_obj(
                ku.element_to_dict(
                    xml_attribs=xml_attribs,
                    element=sc.get_wellbores(
                        q_wellbore=witsml.obj_wellbore(**query_fields),
                        returnElements=return_elements,
                        OptionsIn=options_in,
                    ),
                )
            )
            if return_elements == 'all' and xml_attribs == True:
                if 'wellbore' in wellbores_in_sc['wellbores']:
                    if type(wellbores_in_sc['wellbores']['wellbore']) is list:
                        wellbores_p = []
                        for wellbore in wellbores_in_sc['wellbores'][
                            'wellbore'
                        ]:
                            wellbore['md'] = check_key(
                                check_key(wellbore, 'md'), '#text'
                            )
                            wellbore['tvd'] = check_key(
                                check_key(wellbore, 'tvd'), '#text'
                            )
                            wellbore['mdKickoff'] = check_key(
                                check_key(wellbore, 'mdKickoff'), '#text'
                            )
                            wellbore['mdPlanned'] = check_key(
                                check_key(wellbore, 'mdPlanned'), '#text'
                            )
                            wellbores_p.append(wellbore)
                        wellbores_in_sc['wellbores']['wellbore'] = wellbores_p
                    elif (
                        type(wellbores_in_sc['wellbores']['wellbore']) is dict
                    ):
                        wellbores_in_sc['wellbores']['wellbore'][
                            'md'
                        ] = check_key(
                            check_key(
                                wellbores_in_sc['wellbores']['wellbore'], 'md'
                            ),
                            '#text',
                        )
                        wellbores_in_sc['wellbores']['wellbore'][
                            'tvd'
                        ] = check_key(
                            check_key(
                                wellbores_in_sc['wellbores']['wellbore'], 'tvd'
                            ),
                            '#text',
                        )
                        wellbores_in_sc['wellbores']['wellbore'][
                            'mdKickoff'
                        ] = check_key(
                            check_key(
                                wellbores_in_sc['wellbores']['wellbore'],
                                'mdKickoff',
                            ),
                            '#text',
                        )
                        wellbores_in_sc['wellbores']['wellbore'][
                            'mdPlanned'
                        ] = check_key(
                            check_key(
                                wellbores_in_sc['wellbores']['wellbore'],
                                'mdPlanned',
                            ),
                            '#text',
                        )
            return wellbores_in_sc
        except PyXBException as err:
            raise HTTPException(status_code=422, detail=str(err))
        except (RequestException, StoreException) as err:
            raise HTTPException(
                status_code=502,
                detail=f'{str(err)} or the query has a larger response than supported.',
            )
        except Exception as err:
            raise WitsmlConsumerApiError(str(err)) from err


wellbore = CRUDWellbore()
