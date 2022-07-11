# -*- coding: utf-8 -*-
"""Implementation of the capability routers."""
from typing import Any

from fastapi import APIRouter

from witsml_consumer_api import crud, schemas

router = APIRouter()


@router.get('/capabilities/')
async def read_capabilities() -> Any:
    """
    Retrieve capabilities.
    """

    return crud.capability.get()
