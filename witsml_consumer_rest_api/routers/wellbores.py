# -*- coding: utf-8 -*-
"""Implementation of the wellbore routers."""
from typing import Any

from fastapi import APIRouter

from witsml_consumer_rest_api import crud, schemas

router = APIRouter()


@router.post('/wellbores/')
async def read_wellbores(query_fields_in: schemas.Wellbore) -> Any:
    """
    Retrieve wellbores.
    """

    return crud.wellbore.get(query_fields=query_fields_in)
