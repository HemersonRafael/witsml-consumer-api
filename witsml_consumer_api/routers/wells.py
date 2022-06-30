# -*- coding: utf-8 -*-
"""Implementation of the well routers."""
from typing import Any

from fastapi import APIRouter

from witsml_consumer_api import crud, schemas

router = APIRouter()


@router.post('/wells/')
async def read_wells(query_fields_in: schemas.Well) -> Any:
    """
    Retrieve wells.
    """

    return crud.well.get(query_fields=query_fields_in)
