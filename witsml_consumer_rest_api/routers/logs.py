# -*- coding: utf-8 -*-
"""Implementation of the log routers."""
from typing import Any

from fastapi import APIRouter

from witsml_consumer_rest_api import crud, schemas

router = APIRouter()


@router.post('/logs/')
async def read_logs(query_fields_in: schemas.Log) -> Any:
    """
    Retrieve logs.
    """

    return crud.log.get(query_fields=query_fields_in)
